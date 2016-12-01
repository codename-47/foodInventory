from __future__ import unicode_literals
from django.db import models

class Food_Menu(models.Model):
	def __str__(self):
		return self.name

	food_id = models.AutoField(primary_key=True)
	Yes = 'Yes'
	No = 'No'
	choice = ((Yes, 'Yes'),(No, 'No'))
	name = models.CharField(max_length=200)
	#image = models.BinaryField()
	description = models.TextField(default='Enter description here')
	veg = models.CharField(max_length=4, choices=choice, default=Yes)
