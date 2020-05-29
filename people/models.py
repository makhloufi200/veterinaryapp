from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.
# debtor  مدين
# convicted  مدان
# amount debt  مبلغ الدين
#STATE_PEOPLE = (("Supplier","Supplier"),
#				  ("Customer","Customer"))
class Customer(models.Model):
	name = models.CharField(max_length=100)
	telephone_number = models.CharField(max_length=10, null=True)
	telephone_number1 = models.CharField(max_length=10)
	email = models.CharField(max_length=40, null=True)
	address = models.CharField(max_length=100)
	#type_people = models.CharField(max_length=15, choices=STATE_PEOPLE, default='Customer')
	transaction_amount = models.DecimalField(max_digits=8,decimal_places=2,default=None,null=True)
	
	class Meta:
		ordering = ('name', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('people', args=[self.slug])
		
	def __str__(self):
		return self.name
		
class Supplier(models.Model):
	name = models.CharField(max_length=100)
	telephone_number = models.CharField(max_length=10, null=True)
	telephone_number1 = models.CharField(max_length=10)
	email = models.CharField(max_length=40, null=True)
	address = models.CharField(max_length=100)
	transaction_amount = models.DecimalField(max_digits=8,decimal_places=2,default=None,null=True)
	#type_people = models.CharField(max_length=15, choices=STATE_PEOPLE, default='Customer')
	
	
	class Meta:
		ordering = ('name', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('people', args=[self.slug])
		
	def __str__(self):
		return self.name		