from django.shortcuts import render
from blog.models import Article
# Create your views here.
def blog(request):
	article = Article.objects.all()
#	article['image'] = article['image'][1:]
	return render(request, "blog/blog.html", { "article" : article })