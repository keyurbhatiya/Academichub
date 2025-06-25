from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]
UNIVERSITY_CHOICES = [
    ('GTU', 'Gujarat Technological University'),
    ('HNGU', 'Hemchandracharya North Gujarat University'),
    ('other', 'Other'),  # Add more universities as needed
    # Add more as needed
]

class OldPaper(models.Model):
    title = models.CharField(max_length=200)
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES)
    course = models.CharField(max_length=100)  
    semester = models.CharField(max_length=50)
    file = models.FileField(upload_to='papers/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    semester = models.CharField(max_length=50)
    zip_file = models.FileField(upload_to='projects/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title