from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
# Create your models here.

class Animals(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, blank=True)
	#created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('name', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('animal', args=[self.slug])
		
	def __str__(self):
		return self.name