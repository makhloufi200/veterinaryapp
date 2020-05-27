from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.

STATE_MEDICINE = (("Available","Available"),
				  ("Not Available","Not Available"))
class Medicine(models.Model):
	name = models.CharField(max_length=100)
	#made_in = models.CharField(max_length=100)
	#date_made = models.DateField(null=True,default=None, blank=True)
	#date_expired = models.DateField(null=True,default=None, blank=True)
	quantity = models.IntegerField(default=0)
	#prix_achat_unite = models.DecimalField(max_digits=8,decimal_places=2)
	sale_price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	#test_money_field = models.MoneyField(decimal_places=2,default=0,default_currency='USD',max_digits=8)
	#somme_money = models.DecimalField(max_digits=8,decimal_places=2)
	#delai_attente = models.IntegerField()
	status = models.CharField(max_length=15, choices=STATE_MEDICINE, default='Not Available')
	
	class Meta:
		ordering = ('name', )

	def save(self, *args, **kwargs):
		
		if not self.id:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('medicine', args=[self.slug])
		
	def __str__(self):
		return self.name