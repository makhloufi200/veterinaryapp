from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice,MedicationBill

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number','date_opp','customer','animal','number_animal','address']
		
class MedicationBillForm(forms.ModelForm):
    class Meta:
        model = MedicationBill
        fields = ['invoice','medecine','quantity_medicine','sale_price']		