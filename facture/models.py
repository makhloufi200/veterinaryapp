from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from medicine.models import Medicine
from people.models import Supplier
from animal.models import Animals
from django.shortcuts import render, redirect, get_object_or_404
# Create your models here.

		
class Invoice(models.Model):
	
	date_opp = models.DateField(null=True,default=None, blank=True)
	customer = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
	number_animal = models.IntegerField()
	address = models.CharField(max_length=100)
	total_price = models.DecimalField(max_digits=8,decimal_places=2,default=None,null=True)
	#slug = models.SlugField(unique=True, blank=True)
	invoice_number = models.CharField(max_length=10,null=True,default=None, blank=True)
	
	class Meta:
		ordering = ('date_opp', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.invoice_number)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('invoice', args=[self.slug])
		
	def __str__(self):
		return self.invoice_number
		
		
class MedicationBill(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoices')
	medecine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
	quantity_medicine = models.IntegerField()
	sale_price = models.DecimalField(max_digits=8,decimal_places=2)
	total_price = models.DecimalField(max_digits=8,decimal_places=2)
	
	class Meta:
		ordering = ('invoice', )
	
	
	def save(self, *args, **kwargs):
		if (self.medecine.quantity > 0) and (self.quantity_medicine <= self.medecine.quantity):
			self.sale_price = self.medecine.sale_price
			self.total_price = (self.quantity_medicine) * (self.medecine.sale_price)
			self.medecine.quantity = (self.medecine.quantity) - (self.quantity_medicine)
			if self.medecine.quantity <= 0:
				self.medecine.status = "Not Disponible"
			self.medecine.save()
			if not self.id:
				self.slug = slugify(self.invoice)
			super().save(*args, **kwargs)
			if self.invoice.total_price is None:
				self.invoice.total_price = 0
			self.invoice.total_price = (self.invoice.total_price) + (self.total_price)
			self.invoice.save()

	def get_absolute_url(self):
		return reverse_lazy('medicationbill', args=[self.slug])
		
	def __str__(self):
		return self.invoice