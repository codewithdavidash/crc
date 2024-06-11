from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'leading-9 w-full border rounded'
            }),
        }
        
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['img', 'title', 'intro', 'body']
        
        
class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['img', 'title', 'intro', 'body']