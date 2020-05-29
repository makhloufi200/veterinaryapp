from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BuyMedicine

class StockForm(forms.ModelForm):
    class Meta:
        model = BuyMedicine
        fields = ['medicine','date_achat','date_made','date_expired','quantite','prix_achat_unite','prix_vent','delai_attente','supplier']