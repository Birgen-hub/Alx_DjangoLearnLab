from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

# NEW: Define a custom TagWidget for aesthetic/functional separation, inheriting from standard TextInput.
class TagWidget(forms.TextInput):
    """A custom widget to specifically handle tag input, often styled 
    via custom JavaScript/CSS to look like token fields or colored inputs."""
    pass

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            # UPDATED: Use the custom TagWidget for the 'tags' field
            'tags': TagWidget(attrs={'placeholder': 'Enter tags separated by commas (e.g., python, django, tutorial)'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Your Comment'}
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
