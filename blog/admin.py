from django.contrib import admin
from blog.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['subject', 'pub_date', 'is_fresh']

admin.site.register(Article, ArticleAdmin)