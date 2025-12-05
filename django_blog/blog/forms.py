from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class TagWidget(forms.Textarea):
    pass

class PostForm(forms.ModelForm):
    tags = forms.CharField(label='Tags', required=False, help_text='Enter tags separated by commas.')

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'content',
            'tags',
            Submit('submit', 'Save Post', css_class='btn btn-success')
        )
