from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.

STATE_PEOPLE = (("Fornisseur","Fornisseur"),
				  ("Client","Client"))
class People(models.Model):
	name = models.CharField(max_length=100)
	telephone_number = models.CharField(max_length=10, null=True)
	telephone_number1 = models.CharField(max_length=10)
	email = models.CharField(max_length=40, null=True)
	address = models.CharField(max_length=100)
	type_people = models.CharField(max_length=15, choices=STATE_PEOPLE, default='Client')
	
	
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