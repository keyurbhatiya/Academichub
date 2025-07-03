from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

UNIVERSITY_CHOICES = [
    ('GTU', 'Gujarat Technological University'),
    ('HNGU', 'Hemchandracharya North Gujarat University'),
    ('SPU', 'Sardar Patel University'),
    ('MSU', 'The Maharaja Sayajirao University of Baroda'),
    ('GU', 'Gujarat University'),
    ('PU', 'Parul University'),
    ('NFSU', 'National Forensic Sciences University'),
    ('KSU', 'Krantiguru Shyamji Krishna Verma Kachchh University'),
    ('PDPU', 'Pandit Deendayal Energy University (formerly PDPU)'),
    ('DGU', 'Dharmsinh Desai University'),
    ('SU', 'Sumandeep Vidyapeeth'),
    ('RKDU', 'Raksha Shakti University'),
    ('UKU', 'Uka Tarsadia University'),
    ('CU', 'Charotar University of Science and Technology (CHARUSAT)'),
    ('INDU', 'Indian Institute of Teacher Education (IITE)'),
    ('DAIICT', 'Dhirubhai Ambani Institute of Information and Communication Technology'),
    ('NID', 'National Institute of Design'),
    ('IITGN', 'Indian Institute of Technology Gandhinagar'),
    ('IIM', 'Indian Institute of Management Ahmedabad'),
    ('AIIMS', 'All India Institute of Medical Sciences Rajkot'),
    ('GNLU', 'Gujarat National Law University'),
    ('SVNIT', 'Sardar Vallabhbhai National Institute of Technology, Surat'),
    ('VU', 'Vidyapith Universities (Gujarat Vidyapith, Saurashtra University, etc.)'),
    ('other', 'Other'),
]

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('C', 'C'),
    ('C++', 'C++'),
    ('C#', 'C#'),
    ('JavaScript', 'JavaScript'),
    ('TypeScript', 'TypeScript'),
    ('PHP', 'PHP'),
    ('Ruby', 'Ruby'),
    ('Go', 'Go'),
    ('Swift', 'Swift'),
    ('Kotlin', 'Kotlin'),
    ('R', 'R'),
    ('Dart', 'Dart'),
    ('Rust', 'Rust'),
    ('SQL', 'SQL'),
    ('Shell', 'Shell'),
    ('Perl', 'Perl'),
    ('MATLAB', 'MATLAB'),
    ('Scala', 'Scala'),
    ('Haskell', 'Haskell'),
    ('Objective-C', 'Objective-C'),
    ('Visual Basic', 'Visual Basic'),
    ('Assembly', 'Assembly'),
    ('Other', 'Other'),
]

COURSE_CHOICES = [
    ('B.Tech', 'Bachelor of Technology'),
    ('M.Tech', 'Master of Technology'),
    ('Diploma', 'Diploma in Engineering'),
    ('B.E', 'Bachelor of Engineering'),
    ('M.E', 'Master of Engineering'),
    ('BCA', 'Bachelor of Computer Applications'),
    ('MCA', 'Master of Computer Applications'),
    ('BBA', 'Bachelor of Business Administration'),
    ('MBA', 'Master of Business Administration'),
    ('B.Com', 'Bachelor of Commerce'),
    ('M.Com', 'Master of Commerce'),
    ('B.Sc', 'Bachelor of Science'),
    ('M.Sc', 'Master of Science'),
    ('B.A', 'Bachelor of Arts'),
    ('M.A', 'Master of Arts'),
    ('B.Ed', 'Bachelor of Education'),
    ('M.Ed', 'Master of Education'),
    ('LLB', 'Bachelor of Law'),
    ('LLM', 'Master of Law'),
    ('B.Pharm', 'Bachelor of Pharmacy'),
    ('M.Pharm', 'Master of Pharmacy'),
    ('B.Arch', 'Bachelor of Architecture'),
    ('BFA', 'Bachelor of Fine Arts'),
    ('BJMC', 'Bachelor of Journalism and Mass Communication'),
    ('B.P.Ed', 'Bachelor of Physical Education'),
    ('M.P.Ed', 'Master of Physical Education'),
    ('BDS', 'Bachelor of Dental Surgery'),
    ('BHMS', 'Bachelor of Homeopathic Medicine and Surgery'),
    ('B.Voc', 'Bachelor of Vocation'),
    ('B.Lib.I.Sc', 'Bachelor of Library and Information Science'),
    ('M.Lib', 'Master of Library Science'),
    ('M.Phil', 'Master of Philosophy'),
    ('Ph.D', 'Doctor of Philosophy'),
    ('PGD', 'Post Graduate Diploma'),
    ('Diploma (Other)', 'Diploma (Others)'),
]


class OldPaper(models.Model):
    title = models.CharField(max_length=200)
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES)
    course = models.CharField(max_length=100, choices= COURSE_CHOICES)  
    semester = models.CharField(max_length=50)
    file = models.FileField(upload_to='papers/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='approved')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    semester = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='other')  #New field
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # ✅ New field
    zip_file = models.FileField(upload_to='projects/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='approved')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # new
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='approved')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while Blog.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'


class SiteSettings(models.Model):
    website_name = models.CharField(max_length=100, default='AcademicHub')
    contact_email = models.EmailField(default='admin@academichub.com')
    allow_registrations = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)

    def __str__(self):
        return "Site Settings"  

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact from {self.name} ({self.email})'