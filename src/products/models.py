import random
import os
from django.db import models

def get_filename

def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename=random.randint(1,39868478)
	return 

class Product(models.Model): #Product_Category
	title 		=	models.CharField(max_length=120)
	description	=	models.TextField()
	price 		=	models.DecimalField(decimal_places=2,max_digits=20, default=39.99)
	image		=	models.FileField(upload_to='products/', null=True, blank=False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title
