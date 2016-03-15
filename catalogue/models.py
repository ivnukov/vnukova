 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
	section = models.CharField(max_length = 1, choices = (('T','Томаты'),('V','Овощи'),('D', 'Декоративные')))
	name = models.CharField(max_length = 255)
	extra = models.CharField(max_length = 3, choices = (('ind', 'Индетерминантные'), ('pin', 'Полуиндетерминантные'), ('det', 'Детерминантные')), blank = True, null = True)
	description = models.TextField()
	price = models.CharField(max_length = 255)
	imagename = models.FileField(upload_to = 'static/images/catalogue/', null = True, blank = True, default = 'default.jpg')

	def __unicode__(self):
		return self.name


class Cart(models.Model):
	owner = models.CharField(max_length=50)
	product = models.ForeignKey(Item, null=True, default=None)
	quantity = models.PositiveIntegerField(null=True, default = 1)

	def cost(self):
		return int(self.product.price)*int(self.quantity)

	def increase_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()		

class Email(models.Model):
    email = models.EmailField()
