from django import forms
from .models import Post, Comment

class TagWidget(forms.Textarea):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'tags': TagWidget(),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }
