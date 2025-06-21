from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OldPaper, Project, Blog

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OldPaperForm(forms.ModelForm):
    class Meta:
        model = OldPaper
        fields = ['title', 'university', 'semester', 'file']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'semester', 'zip_file']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class ContentModerationForm(forms.Form):
    content_type = forms.ChoiceField(choices=[('paper', 'Paper'), ('project', 'Project'), ('blog', 'Blog')])
    content_id = forms.IntegerField()
    action = forms.ChoiceField(choices=[('approve', 'Approve'), ('reject', 'Reject')])
    reason = forms.CharField(widget=forms.Textarea, required=False)

