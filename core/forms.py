from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django import forms
from .models import *


BLOG_INPUT_CLASSES = """
    block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6
"""


class LoginForm(AuthenticationForm):
    pass


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title', 'profile_pic', 'address', 'phone']
        widgets = {
            "title": forms.Select(attrs={
                'class': BLOG_INPUT_CLASSES
            }),
            "profile_pic": forms.FileInput(attrs={
                'class': BLOG_INPUT_CLASSES
            }),
            "address": forms.TextInput(attrs={
                'class': BLOG_INPUT_CLASSES
            }),
            "phone": forms.TextInput(attrs={
                'class': BLOG_INPUT_CLASSES
            }),
        }