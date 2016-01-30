from django.shortcuts import render
from catalogue.models import Item

def index(request):
	item = Item.objects.all()
	return render(request, 'index.html', {'item':item})