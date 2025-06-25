from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm, OldPaperForm, ProjectForm, BlogForm
from .models import OldPaper, Project, Blog
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContentModerationForm
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    # Prepare dynamic data
    universities = OldPaper.objects.values_list('university', flat=True).distinct()
    courses = OldPaper.objects.values_list('course', flat=True).distinct()

    # Context for the template
    context = {
        'total_papers': OldPaper.objects.count(),
        'total_projects': Project.objects.count(),
        'total_blogs': Blog.objects.count(),
        'total_users': User.objects.count(),
        'papers': OldPaper.objects.order_by('-uploaded_at')[:9],
        'universities': universities,
        'courses': courses,
    }
    return render(request, 'core/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def upload_paper(request):
    if request.method == 'POST':
        form = OldPaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.uploaded_by = request.user
            paper.save()
            messages.success(request, 'Paper uploaded successfully!')
            return redirect('papers')
    else:
        form = OldPaperForm()
    return render(request, 'core/upload_paper.html', {'form': form})

@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.uploaded_by = request.user
            project.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'core/upload_project.html', {'form': form})

def papers(request):
    papers = OldPaper.objects.all().order_by('-uploaded_at')
    return render(request, 'core/papers.html', {'papers': papers})

def projects(request):
    projects = Project.objects.all().order_by('-uploaded_at')
    return render(request, 'core/projects.html', {'projects': projects})


def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'core/blogs.html', {'blogs': blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog created successfully!')
            return redirect('blogs')
    else:
        form = BlogForm()
    return render(request, 'core/blog_create.html', {'form': form})


# admin_dashboard view 

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    total_users = User.objects.count()
    total_papers = OldPaper.objects.count()
    total_projects = Project.objects.count()
    total_blogs = Blog.objects.count()
    recent_papers = OldPaper.objects.order_by('-uploaded_at')[:5]
    recent_projects = Project.objects.order_by('-uploaded_at')[:5]
    recent_blogs = Blog.objects.order_by('-created_at')[:5]

    context = {
        'total_users': total_users,
        'total_papers': total_papers,
        'total_projects': total_projects,
        'total_blogs': total_blogs,
        'recent_papers': recent_papers,
        'recent_projects': recent_projects,
        'recent_blogs': recent_blogs,
    }

    # Chart data
    def format_data(queryset):
        return {entry['month'].strftime('%b'): entry['total'] for entry in queryset}

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

    def get_values(data_map):
        return [data_map.get(month, 0) for month in months]

    papers_by_month = OldPaper.objects.annotate(month=TruncMonth('uploaded_at')).values('month').annotate(total=Count('id')).order_by('month')
    projects_by_month = Project.objects.annotate(month=TruncMonth('uploaded_at')).values('month').annotate(total=Count('id')).order_by('month')
    blogs_by_month = Blog.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(total=Count('id')).order_by('month')
    user_growth = User.objects.annotate(month=TruncMonth('date_joined')).values('month').annotate(total=Count('id')).order_by('month')

    context.update({
        'months': json.dumps(months),
        'paper_data': json.dumps(get_values(format_data(papers_by_month))),
        'project_data': json.dumps(get_values(format_data(projects_by_month))),
        'blog_data': json.dumps(get_values(format_data(blogs_by_month))),
        'user_data': json.dumps(get_values(format_data(user_growth))),
        'distribution_data': json.dumps([
            {'value': total_papers, 'name': 'Papers'},
            {'value': total_projects, 'name': 'Projects'},
            {'value': total_blogs, 'name': 'Blogs'},
        ])
    })

    return render(request, 'admin/dashboard.html', context)

@login_required
def admin_users(request):
    # Get query parameters
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'username')
    role_filter = request.GET.getlist('role')  # accepts multiple: admin/user
    status_filter = request.GET.getlist('status')  # accepts multiple: active/inactive

    # Base query
    users = User.objects.all()

    # Search
    if search_query:
        users = users.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))

    # Role Filter
    if 'admin' in role_filter:
        users = users.filter(is_superuser=True)
    if 'user' in role_filter:
        users = users.filter(is_superuser=False)

    # Status Filter
    if 'active' in status_filter:
        users = users.filter(is_active=True)
    if 'inactive' in status_filter:
        users = users.filter(is_active=False)

    # Sorting
    sort_options = {
        'username': 'username',
        'email': 'email',
        'date_joined': 'date_joined',
        'is_active': 'is_active',
        'is_superuser': 'is_superuser'
    }
    users = users.order_by(sort_options.get(sort_by, 'username'))

    # Pagination
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'users': page_obj.object_list,
        'search_query': search_query,
        'role_filter': role_filter,
        'status_filter': status_filter,
        'sort_by': sort_by
    }

    return render(request, 'admin/users.html', context)

@login_required
def admin_papers(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    papers = OldPaper.objects.all().order_by('-uploaded_at')
    return render(request, 'admin/papers.html', {'papers': papers})

@login_required
def admin_projects(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    projects = Project.objects.all().order_by('-uploaded_at')
    return render(request, 'admin/projects.html', {'projects': projects})

@login_required
def admin_blogs(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'admin/blogs.html', {'blogs': blogs})

@login_required
def Content_Moderation(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = ContentModerationForm(request.POST)
        if form.is_valid():
            content_type = form.cleaned_data['content_type']
            content_id = form.cleaned_data['content_id']
            action = form.cleaned_data['action']
            reason = form.cleaned_data['reason']

            model_map = {
                'paper': OldPaper,
                'project': Project,
                'blog': Blog,
            }

            model = model_map.get(content_type)
            if not model:
                messages.error(request, 'Invalid content type.')
                return redirect('content_moderation')

            obj = get_object_or_404(model, id=content_id)
            obj.status = 'Approved' if action == 'approve' else 'Rejected'
            obj.save()

            messages.success(request, f'{content_type.title()} has been {action}d.')
            return redirect('content_moderation')

    else:
        form = ContentModerationForm()

    # Merge and annotate all pending content
    papers = OldPaper.objects.filter(status='Pending').select_related('uploaded_by')
    projects = Project.objects.filter(status='Pending').select_related('uploaded_by')
    blogs = Blog.objects.filter(status='Pending').select_related('author')

    contents = []

    for paper in papers:
        contents.append({
            'id': paper.id,
            'title': paper.title,
            'type': 'Paper',
            'uploader': paper.uploaded_by.username,
            'submitted': paper.uploaded_at,
            'status': paper.status,
        })

    for project in projects:
        contents.append({
            'id': project.id,
            'title': project.title,
            'type': 'Project',
            'uploader': project.uploaded_by.username,
            'submitted': project.uploaded_at,
            'status': project.status,
        })

    for blog in blogs:
        contents.append({
            'id': blog.id,
            'title': blog.title,
            'type': 'Blog',
            'uploader': blog.author.username,
            'submitted': blog.created_at,
            'status': blog.status,
        })

    return render(request, 'admin/content_moderation.html', {
        'form': form,
        'contents': contents
    })



