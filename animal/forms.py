from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Animals

class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['name']