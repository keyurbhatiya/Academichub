from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OldPaper, Project, Blog, Contact, SiteSettings

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OldPaperForm(forms.ModelForm):
    class Meta:
        model = OldPaper
        fields = ['title', 'university', 'course', 'semester', 'file']
        labels = {
            'title': 'Subject',
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'semester', 'language', 'image', 'zip_file'] # New field imgage,language

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

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
