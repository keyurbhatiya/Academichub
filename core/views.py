from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm, OldPaperForm, ProjectForm, BlogForm, ContactForm, FeedbackForm, Feedback
from .models import OldPaper, Project, Blog, SiteSettings,  Comment,Contact
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContentModerationForm
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.db import IntegrityError
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import OperationalError
# telegram
# from core.forms import OldPaperForm
# from .telegram import send_file_to_telegram

def home(request):
    try:
        from django.contrib.auth.models import User
        # Prepare dynamic data
        context = {
        'papers': OldPaper.objects.all()[:6],
        'projects': Project.objects.all()[:4],
        'blogs': Blog.objects.all()[:4],
        'universities': OldPaper.objects.values_list('university', flat=True).distinct(),
        'courses': OldPaper.objects.values_list('course', flat=True).distinct(),
        'total_papers': OldPaper.objects.count(),
        'total_users': User.objects.count(),
        'total_projects': Project.objects.count(),
        'total_contributions': OldPaper.objects.count() + Project.objects.count(),
        }
        return render(request, 'core/home/home.html', context)
    except OperationalError as e:
        error = str(e)
        return render(request, 'auth/error_page/error_page.html', {
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
    semester = request.GET.get('semester')
    
    if university:
        papers = papers.filter(university=university)
    if course:
        papers = papers.filter(course=course)
    if semester:
        papers = papers.filter(semester__icontains=semester)
    
    context = {
        'papers': papers,
        'universities': universities,
        'courses': courses,
        'selected_university': university or '',
        'selected_course': course or '',
        'selected_semester': semester or ''
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Render only the papers list for AJAX requests
        return render(request, 'core/papers/papers_list.html', context)
    
    return render(request, 'core/papers/papers.html', context)

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
            Q(uploaded_by__username__icontains=search_query)
        )

    languages = Project.objects.values_list('language', flat=True).distinct()

    context = {
        'projects': projects,
        'selected_language': selected_language,
        'search_query': search_query,
        'languages': languages
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Render only the projects list for AJAX requests
        return render(request, 'core/projects/projects_list.html', context)
    
    return render(request, 'core/projects/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'core/projects/project_detail.html', {'project': project})

def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'core/blogs/blogs.html', {'blogs': blogs})

def help_center(request):
    return render(request, 'core/help-center/help_center.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact-us/contact.html', {'form': form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user if request.user.is_authenticated else None
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback/feedback.html', {'form': form})

def community_guidelines(request):
    return render(request, 'core/community_guidelines/community_guidelines.html')

def faq_page(request):
    return render(request, 'core/faqs/faq.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/terms_of_service/terms_of_service.html')

def cookie_policy(request):
    return render(request, 'core/cookie_policy/cookie_policy.html')

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

    return render(request, 'core/papers/upload_paper.html', {'form': form})


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

    return render(request, 'core/projects/upload_project.html', {'form': form})


# Create a new blog post view

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
    return render(request, 'core/blogs/blog_create.html', {'form': form})

# blog slug view
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    # Show limited or all comments
    show_all = request.GET.get('show_all_comments') == 'true'
    comments = blog.comments.filter(parent__isnull=True).order_by('-created_at')
    if not show_all:
        comments = comments[:2]

    # Related posts logic (based on similar title words or any other criteria)
    related_posts = Blog.objects.filter(
        Q(title__icontains=blog.title.split()[0]) | Q(status='Published'),
        ~Q(id=blog.id)
    ).distinct()[:3]

    # Fallback: show recent posts if no related ones found
    if not related_posts.exists():
        related_posts =blogs = Blog.objects.all().order_by('-created_at')[:3]

    return render(request, 'core/blogs/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'show_all_comments': show_all,
        'related_posts': related_posts,
    })

# Add comment to blog view
@login_required
def add_comment(request, slug):
    if request.method == 'POST':
        blog = Blog.objects.get(slug=slug)
        Comment.objects.create(
            blog=blog,
            user=request.user if request.user.is_authenticated else None,
            name=request.POST['name'],
            email=request.POST['email'],
            content=request.POST['content'],
        )
        messages.success(request, 'Comment posted successfully!')
        return redirect('blog_detail', slug=slug)
    return redirect('blog_detail', slug=slug)

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user
    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True
    return JsonResponse({
        'likes_count': comment.likes.count(),
        'liked': liked
    })

@login_required
def like_reply(request, reply_id):
    pass
    # reply = get_object_or_404(Reply, id=reply_id)
    # user = request.user
    # if user in reply.likes.all():
    #     reply.likes.remove(user)
    #     liked = False
    # else:
    #     reply.likes.add(user)
    #     liked = True
    # return JsonResponse({
    #     'likes_count': reply.likes.count(),
    #     'liked': liked
    # })

@login_required
def add_reply(request, slug):
    pass

def dislike_blog(request, slug):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, slug=slug)
        blog.dislikes += 1
        blog.save()
        messages.success(request, 'You disliked this blog post.')
    return redirect('blog_detail', slug=slug)

# user profile view
@login_required
def profile_view(request):
    return render(request, 'auth/profile/profile.html')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'auth/profile/password_change.html'
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
    return render(request, 'core/my-upload/user_uploads.html', context)

############################################################# admin views #############################################################

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
    return render(request, 'admin/dashboard/dashboard.html', context)

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

    return render(request, 'admin/user_managment/users.html', context)

@login_required
def add_user(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # use password1
            user.save()
            messages.success(request, f"User {user.username} created successfully.")
            return redirect('admin_users')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'admin/user_managment/add_user.html', {'form': form})

# admin side papers view
@login_required
def admin_papers(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    papers = OldPaper.objects.all().order_by('-uploaded_at')
    return render(request, 'admin/papers/papers.html', {'papers': papers})

# admin side paper upload
@login_required
def admin_upload_old_paper(request):
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

    return render(request, 'admin/papers/papers_upload.html', {'form': form})

# admin side projects view
@login_required
def admin_projects(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    projects = Project.objects.all().order_by('-uploaded_at')
    return render(request, 'admin/projects/projects.html', {'projects': projects})

# admin side project upload

@login_required
def admin_upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.uploaded_by = request.user
            project.status = 'approved'  
            project.save()
            messages.success(request, 'Project uploaded successfully and is pending moderation.')
            return redirect('admin_projects')
        else:
            messages.error(request, 'Please correct the errors below: ' + '; '.join(
                f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()
            ))
    else:
        form = ProjectForm()

    return render(request, 'admin/projects/projects_upload.html', {'form': form})

# admin side project delete
def admin_delete_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        try:
            project_title = project.title
            project.delete()
            messages.success(request, f'Project "{project_title}" deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting project: {str(e)}')
        return redirect('admin_projects')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('admin_projects')

@login_required
def admin_blogs(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'admin/blogs/blogs.html', {'blogs': blogs})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        if blog.uploaded_by == request.user or request.user.is_superuser:
            blog.delete()
            messages.success(request, "Blog deleted successfully.")
            return redirect('admin_blogs')  # Change this to your blog listing URL name
        else:
            messages.error(request, "You are not authorized to delete this blog.")
            return redirect('blog_detail', slug=blog.slug)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully.')
            return redirect('admin_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin/blogs/edit_blog.html', {'form': form, 'blog': blog})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.uploaded_by = request.user
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog created successfully.')
            return redirect('admin_blogs')
    else:
        form = BlogForm()
    return render(request, 'admin/create_blog.html', {'form': form})

@login_required
def Content_Moderation(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
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
            if action == 'reject' and reason:
                obj.rejection_reason = reason  # Assuming models have a rejection_reason field
            obj.save()
            
            messages.success(request, f'{content_type.title()} has been {action}d.')
            return redirect('content_moderation')
    else:
        form = ContentModerationForm()
    
    # Get status filter from GET parameters
    status_filter = request.GET.get('status', 'approved')
    
    # Fetch all content
    papers = OldPaper.objects.all().select_related('uploaded_by')
    projects = Project.objects.all().select_related('uploaded_by')
    blogs = Blog.objects.all().select_related('author')
    
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
    
    # Calculate counts for each status
    pending_count = sum(1 for c in contents if c['status'] == 'Pending')
    approved_count = sum(1 for c in contents if c['status'] == 'Approved')
    rejected_count = sum(1 for c in contents if c['status'] == 'Rejected')
    flagged_count = sum(1 for c in contents if c['status'] == 'Flagged')
    
    # Filter contents based on status
    if status_filter and status_filter != 'all':
        status_map = {
            'pending': 'Pending',
            'approved': 'Approved',
            'rejected': 'Rejected',
            'flagged': 'Flagged'
        }
        filter_status = status_map.get(status_filter.lower())
        if filter_status:
            contents = [c for c in contents if c['status'] == filter_status]
    
    # Sort contents by submitted date (newest first)
    contents.sort(key=lambda x: x['submitted'], reverse=True)
    
    # Pagination
    paginator = Paginator(contents, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'admin/content_moderation/content_moderation.html', {
        'form': form,
        'contents': page_obj,
        'page_obj': page_obj,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'flagged_count': flagged_count,
        'current_status': status_filter,
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def view_user_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'admin/user_managment/user_profile.html')

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


def analytics(request):
    # Summary statistics
    total_users = User.objects.count()
    total_papers = OldPaper.objects.count()
    total_projects = Project.objects.count()
    total_blogs = Blog.objects.count()
    
    # Calculate active users this week (users who logged in within the last 7 days)
    from django.utils import timezone
    from datetime import timedelta
    week_ago = timezone.now() - timedelta(days=7)
    active_users_week = User.objects.filter(last_login__gte=week_ago).count()
    
    # Latest items (e.g., last 5 entries)
    latest_papers = OldPaper.objects.order_by('-uploaded_at')[:5]
    latest_projects = Project.objects.order_by('-uploaded_at')[:5]
    latest_blogs = Blog.objects.order_by('-created_at')[:5]
    
    # Get current year for filtering
    current_year = datetime.now().year
    
    # Chart data - Fixed to get data for the last 6 months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Get monthly data for papers
    paper_monthly = OldPaper.objects.filter(
        uploaded_at__year=current_year
    ).extra({'month': "EXTRACT(month FROM uploaded_at)"}).values('month').annotate(count=Count('id')).order_by('month')
    
    # Get monthly data for projects
    project_monthly = Project.objects.filter(
        uploaded_at__year=current_year
    ).extra({'month': "EXTRACT(month FROM uploaded_at)"}).values('month').annotate(count=Count('id')).order_by('month')
    
    # Get monthly data for blogs
    blog_monthly = Blog.objects.filter(
        created_at__year=current_year
    ).extra({'month': "EXTRACT(month FROM created_at)"}).values('month').annotate(count=Count('id')).order_by('month')
    
    # Get monthly user registrations
    user_monthly = User.objects.filter(
        date_joined__year=current_year
    ).extra({'month': "EXTRACT(month FROM date_joined)"}).values('month').annotate(count=Count('id')).order_by('month')
    
    # Initialize arrays with zeros for all 12 months
    paper_data = [0] * 12
    project_data = [0] * 12
    blog_data = [0] * 12
    user_data = [0] * 12
    
    # Fill in the actual data
    for item in paper_monthly:
        paper_data[int(item['month']) - 1] = item['count']
    
    for item in project_monthly:
        project_data[int(item['month']) - 1] = item['count']
    
    for item in blog_monthly:
        blog_data[int(item['month']) - 1] = item['count']
    
    for item in user_monthly:
        user_data[int(item['month']) - 1] = item['count']
    
    # Distribution data
    distribution_data = [
        {'value': total_papers, 'name': 'Papers'},
        {'value': total_projects, 'name': 'Projects'},
        {'value': total_blogs, 'name': 'Blogs'}
    ]
    
    # User roles data (you may need to adjust this based on your user model)
    user_roles_data = [
        {'value': User.objects.filter(is_staff=True, is_superuser=False).count(), 'name': 'Staff'},
        {'value': User.objects.filter(is_superuser=True).count(), 'name': 'Admin'},
        {'value': User.objects.filter(is_staff=False, is_superuser=False).count(), 'name': 'Regular Users'}
    ]
    
    context = {
        'total_users': total_users,
        'total_papers': total_papers,
        'total_projects': total_projects,
        'total_blogs': total_blogs,
        'active_users_week': active_users_week,
        'latest_papers': latest_papers,
        'latest_projects': latest_projects,
        'latest_blogs': latest_blogs,
        'months': json.dumps(months),
        'paper_data': json.dumps(paper_data),
        'project_data': json.dumps(project_data),
        'blog_data': json.dumps(blog_data),
        'user_data': json.dumps(user_data),
        'distribution_data': json.dumps(distribution_data),
        'user_roles_data': json.dumps(user_roles_data),
    }
    
    return render(request, 'admin/analytics/analytics.html', context)

def settings(request):
    settings_obj, created = SiteSettings.objects.get_or_create()
    if request.method == 'POST':
        settings_obj.website_name = request.POST.get('website_name', settings_obj.website_name)
        settings_obj.contact_email = request.POST.get('contact_email', settings_obj.contact_email)
        settings_obj.allow_registrations = request.POST.get('allow_registrations') == 'on'
        settings_obj.email_notifications = request.POST.get('email_notifications') == 'on'
        settings_obj.save()
        messages.success(request, 'Settings updated successfully.')
        return redirect('settings')
    context = {'settings': settings_obj}
    return render(request, 'admin/settings/settings.html', context)

# admin contact us view
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact_us(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        action = request.POST.get('action')
        contact = get_object_or_404(Contact, id=contact_id)
        
        if action == 'review':
            try:
                contact.status = 'Reviewed'
                contact.save()
                messages.success(request, f'Contact message ID {contact.id} marked as Reviewed.')
            except Exception as e:
                messages.error(request, f'Error updating contact message: {str(e)}')
            return redirect('admin_contact_us')

    contact_list = Contact.objects.all().order_by('-created_at')
    contact_count = contact_list.count()
    pending_count = contact_list.filter(status='Pending').count()
    reviewed_count = contact_list.filter(status='Reviewed').count()

    context = {
        'contact_list': contact_list,
        'contact_count': contact_count,
        'pending_count': pending_count,
        'reviewed_count': reviewed_count,
    }
    return render(request, 'admin/contact_us/contact_us.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_contact(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, id=contact_id)
        try:
            contact_id = contact.id
            contact.delete()
            messages.success(request, f'Contact message ID {contact_id} deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting contact message: {str(e)}')
        return redirect('admin_contact_us')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('admin_contact_us')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_feedback(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        action = request.POST.get('action')
        feedback = get_object_or_404(Feedback, id=feedback_id)
        
        if action == 'review':
            try:
                feedback.status = 'Reviewed'
                feedback.save()
                messages.success(request, f'Feedback ID {feedback.id} marked as Reviewed.')
            except Exception as e:
                messages.error(request, f'Error updating feedback: {str(e)}')
            return redirect('admin_feedback')

    feedback_list = Feedback.objects.all().order_by('-created_at')
    feedback_count = feedback_list.count()
    pending_count = feedback_list.filter(status='Pending').count()
    reviewed_count = feedback_list.filter(status='Reviewed').count()

    context = {
        'feedback_list': feedback_list,
        'feedback_count': feedback_count,
        'pending_count': pending_count,
        'reviewed_count': reviewed_count,
    }
    return render(request, 'admin/feedback/feedback.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, id=feedback_id)
        try:
            feedback_id = feedback.id
            feedback.delete()
            messages.success(request, f'Feedback ID {feedback_id} deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting feedback: {str(e)}')
        return redirect('admin_feedback')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('admin_feedback')
    
