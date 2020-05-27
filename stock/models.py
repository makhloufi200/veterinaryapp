from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from medicine.models import Medicine
from people.models import People
from animal.models import Animals
from django.shortcuts import render, redirect, get_object_or_404
# Create your models here.


class AchatMedecine(models.Model):
	medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
	date_achat = models.DateField(null=True,default=None, blank=True)
	date_made = models.DateField(null=True,default=None, blank=True)
	date_expired = models.DateField(null=True,default=None, blank=True)
	quantite = models.IntegerField()
	prix_achat_unite = models.DecimalField(max_digits=8,decimal_places=2)
	prix_vent = models.DecimalField(max_digits=8,decimal_places=2)
	#test_money_field = models.MoneyField(decimal_places=2,default=0,default_currency='USD',max_digits=8)
	somme_money = models.DecimalField(max_digits=8,decimal_places=2)
	delai_attente = models.IntegerField()
	fornisseur = models.ForeignKey(People, on_delete=models.CASCADE)

	
	
	class Meta:
		ordering = ('date_achat', )

	def save(self, *args, **kwargs):
		self.somme_money = (self.quantite) * (self.prix_achat_unite)
		self.medicine.quantity = (self.medicine.quantity) + (self.quantite)
		self.medicine.sale_price = self.prix_vent
		if self.medicine.quantity >= 0 :
			self.medicine.status = 'Available'
			self.medicine.save()
		if not self.id:
			self.slug = slugify(self.medicine)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('achat', args=[self.slug])
		
	def __str__(self):
		return self.medicine
		
	
	