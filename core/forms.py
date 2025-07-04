from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OldPaper, Project, Blog, Contact, SiteSettings, Feedback

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


