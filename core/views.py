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
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import OperationalError

def home(request):
    try:
        from django.contrib.auth.models import User
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
    except OperationalError as e:
        error = str(e)
        return render(request, 'auth/error_page.html', {
            'error': error,
            'data': None,
        })
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

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
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def papers(request):

    papers = OldPaper.objects.all().order_by('-uploaded_at')
    
    universities = OldPaper.objects.values_list('university', flat=True).distinct()
    courses = OldPaper.objects.values_list('course', flat=True).distinct()

    university = request.GET.get('university')
    course = request.GET.get('course')
    
    if university:
        papers = papers.filter(university=university)
    if course:
        papers = papers.filter(course=course)
    
    return render(request, 'core/papers.html', {
        'papers': papers,
        'universities': universities,
        'courses': courses
    })

def projects(request):
    selected_language = request.GET.get('language', '')
    search_query = request.GET.get('search', '')

    projects = Project.objects.all().order_by('-uploaded_at')

    if selected_language:
        projects = projects.filter(language=selected_language)

    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(uploaded_by__username__icontains=search_query)  # 👈 fix here
        )

    languages = Project.objects.values_list('language', flat=True).distinct()

    context = {
        'projects': projects,
        'selected_language': selected_language,
        'search_query': search_query,
        'languages': languages
    }

    return render(request, 'core/projects.html', context)

def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'core/blogs.html', {'blogs': blogs})

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
            return redirect('projects')  # Adjust URL name if needed
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProjectForm()

    return render(request, 'core/upload_project.html', {'form': form})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.uploaded_by = request.user
            blog.author = request.user  # Add this line
            blog.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('blogs')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BlogForm()
    return render(request, 'core/blog_create.html', {'form': form})

# user profile view
@login_required
def profile_view(request):
    return render(request, 'auth/profile.html')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'auth/password_change.html'
    success_url = reverse_lazy('profile')  # Redirect to profile page after success

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your password was successfully changed!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Please correct the errors below.")
        return response


# user_uploads data view
@login_required
def user_uploads_view(request):
    user = request.user
    papers = OldPaper.objects.filter(uploaded_by=user)
    projects = Project.objects.filter(uploaded_by=user)
    blogs = Blog.objects.filter(author=user)

    context = {
        'papers': papers,
        'projects': projects,
        'blogs': blogs,
    }
    return render(request, 'core/user_uploads.html', context)

# admin_dashboard view 

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    # Summary statistics
    total_users = User.objects.count()
    total_papers = OldPaper.objects.count()
    total_projects = Project.objects.count()
    total_blogs = Blog.objects.count()
    total_downloads = 12500  # Replace with actual logic if available

    # Latest items (e.g., last 5 entries)
    latest_papers = OldPaper.objects.order_by('-uploaded_at')[:5]
    latest_projects = Project.objects.order_by('-uploaded_at')[:5]
    latest_blogs = Blog.objects.order_by('-created_at')[:5]

    # Chart data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    paper_data = [OldPaper.objects.filter(uploaded_at__month=i+1).count() for i in range(1, 7)]
    project_data = [Project.objects.filter(uploaded_at__month=i+1).count() for i in range(1, 7)]
    blog_data = [Blog.objects.filter(created_at__month=i+1).count() for i in range(1, 7)]
    user_data = [User.objects.filter(date_joined__month=i+1).count() for i in range(1, 7)]
    distribution_data = [
        {'value': total_papers, 'name': 'Papers'},
        {'value': total_projects, 'name': 'Projects'},
        {'value': total_blogs, 'name': 'Blogs'}
    ]

    context = {
        'total_users': total_users,
        'total_papers': total_papers,
        'total_projects': total_projects,
        'total_blogs': total_blogs,
        'total_downloads': total_downloads,
        'latest_papers': latest_papers,
        'latest_projects': latest_projects,
        'latest_blogs': latest_blogs,
        'months': json.dumps(months),
        'paper_data': json.dumps(paper_data),
        'project_data': json.dumps(project_data),
        'blog_data': json.dumps(blog_data),
        'user_data': json.dumps(user_data),
        'distribution_data': json.dumps(distribution_data),
    }
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def view_user_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'admin/user_profile.html', {'user_profile': user_profile})

# Deactivate user view
@login_required
@user_passes_test(lambda u: u.is_superuser)
def deactivate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f'User {user.username} has been deactivated.')
    return redirect('admin_users')

# Activate user view
@login_required
@user_passes_test(lambda u: u.is_superuser)
def activate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, f"{user.username} has been activated.")
    else:
        messages.info(request, f"{user.username} is already active.")
    return redirect('admin_users')  # Redirect to your user management page

# error page view

def some_view(request):
    error = None
    data = None
    try:
        # Some DB operation
        from django.contrib.auth.models import User
        data = User.objects.all()  # Example DB call
    except OperationalError as e:
        error = str(e)

    return render(request, 'auth/error_page.html', {
        'error': error,
        'data': data,
    })

# admin side paper upload
def upload_old_paper(request):
    if request.method == 'POST':
        form = OldPaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.uploaded_by = request.user
            paper.save()
            messages.success(request, 'Paper uploaded successfully!')
            return redirect('admin_papers')
    else:
        form = OldPaperForm()

    return render(request, 'admin/papers_upload.html', {'form': form})

