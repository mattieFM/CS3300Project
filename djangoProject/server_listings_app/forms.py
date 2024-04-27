from django.db import models
from django.forms import ModelForm
from django.contrib.auth import forms as auth_forms
from django import forms
from .models import *


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ["title", "description", "password", "is_active"]

class UpdateUserForm(ModelForm):
    """A form to update users"""
    bio = forms.CharField(required=False, widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'bio']


class NewUserForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    """A form to register new users"""
    bio = forms.CharField(required=False, widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']