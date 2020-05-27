from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import People


class PeopleForm(forms.ModelForm):
	class Meta:
		model = People
		fields = ['name','telephone_number','telephone_number1','email','address','type_people']