from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OldPaper, Project, Blog, Contact, SiteSettings, Feedback
from django import forms
from django.core.validators import URLValidator
import re
import requests

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OldPaperForm(forms.ModelForm):
    class Meta:
        model = OldPaper
        fields = ['title', 'university', 'course', 'semester', 'drive_url']
        labels = {
            'title': 'Subject',
            'drive_url': 'Google Drive URL'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Data Structures & Algorithms'}),
            'university': forms.Select(),
            'course': forms.Select(),
            'semester': forms.Select(choices=[(i, f'Semester {i}') for i in range(1, 9)]),
            'drive_url': forms.URLInput(attrs={'placeholder': 'https://drive.google.com/...'}),
        }

    def clean_drive_url(self):
        drive_url = self.cleaned_data.get('drive_url')
        if not drive_url:
            return drive_url

        # Validate URL format
        validator = URLValidator()
        validator(drive_url)

        # Check if it's a Google Drive URL
        if not re.match(r'^https?://(drive|docs)\.google\.com/', drive_url):
            raise forms.ValidationError("Please provide a valid Google Drive URL.")

        # Optional: Check if the file is accessible (basic check)
        try:
            response = requests.head(drive_url, allow_redirects=True, timeout=5)
            if response.status_code != 200:
                raise forms.ValidationError("The provided URL is not accessible. Ensure the file is shared with 'Anyone with the link'.")
        except requests.RequestException:
            raise forms.ValidationError("Unable to verify the URL. Please ensure it's correct and accessible.")

        return drive_url


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'semester', 'language', 'image', 'github_url']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'id': 'blog-content-editor'}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class ContentModerationForm(forms.Form):
    content_type = forms.ChoiceField(choices=[('paper', 'Paper'), ('project', 'Project'), ('blog', 'Blog')])
    content_id = forms.IntegerField()
    action = forms.ChoiceField(choices=[('approve', 'Approve'), ('reject', 'Reject')])
    reason = forms.CharField(widget=forms.Textarea, required=False)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your feedback'})
        }


# In your forms.py
def clean_file(self):
    file = self.cleaned_data.get('file')
    if file:
        if file.size > 10 * 1024 * 1024:  # 10MB limit
            raise forms.ValidationError("File size cannot exceed 10MB")
    return file


