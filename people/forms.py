from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Supplier


class PeopleForm(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = ['name','telephone_number','telephone_number1','email','address']