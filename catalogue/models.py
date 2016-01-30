 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Item(models.Model):
	section = models.CharField(max_length = 1, choices = (('T','Томаты'),('V','Овощи'),('D', 'Декоративные')))
	name = models.CharField(max_length = 255)
	extra = models.CharField(max_length = 3, choices = (('ind', 'Индетерминантные'), ('pin', 'Полуиндетерминантные'), ('det', 'Детерминантные')), blank = True, null = True)
	description = models.TextField()
	price = models.CharField(max_length = 255)
	imagename = models.FileField(upload_to = 'static/images/catalogue/', null = True, blank = True)

	def __unicode__(self):
		return self.name
