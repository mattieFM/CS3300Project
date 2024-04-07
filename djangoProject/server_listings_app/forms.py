from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ["title", "description", "password", "is_active"]
