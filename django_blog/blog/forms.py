from django import forms
from .models import Post

class TagWidget(forms.Textarea):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Enter tags separated by commas...'}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }
