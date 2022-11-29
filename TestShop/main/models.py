from django.db import models

class Item(models.Model):
	name = models.CharField('name', max_length=50)
	description = models.TextField('description')
	price = models.DecimalField('price', max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name
