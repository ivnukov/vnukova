from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from pytils.translit import slugify
from django.conf import settings

class Article(models.Model):
	subject = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	pub_date = models.DateTimeField(auto_now_add =True)
	text = models.TextField()
	shorturl = models.CharField(max_length=255)
	image1 = models.FileField(upload_to = 'static/images/blog/', null = True, blank = True)
	image2 = models.FileField(upload_to = 'static/images/blog/', null = True, blank = True)
	image3 = models.FileField(upload_to = 'static/images/blog/', null = True, blank = True)
	image = models.FileField(upload_to = 'static/images/blog/', null = True, blank = True)
	def is_fresh(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)  		