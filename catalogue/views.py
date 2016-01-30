from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalogue.models import Item
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


# Create your views here.
def main(request):
	item = Item.objects.all()
	return render(request, 'catalogue/catalogue.html', {'item': item})

def list_view(request, section_id):
	if section_id == "A":
		item = Item.objects.all()
	else:
		item = Item.objects.filter(section = section_id)
	return render(request, 'catalogue/list_view.html', {'item': item})

#class ItemDetailView(DetailView):
#	model = Item
#	template_name = "catalogue/detail.html"
#	def get_context_data(self, **kwargs):
#		context = super(ItemDetailView, self).get_context_data(**kwargs)
#		return context

# this stuff goes at the top of the file, below other imports

# new product view, with POST vs GET detection

def show_product(request, pk, template_name="catalogue/detail.html"):
	p = get_object_or_404(Item, id=pk)
	description = p.description
	extra = p.extra
	price = p.price
	name = p.name
	imagename = p.imagename	
	return render_to_response(template_name, locals(), context_instance=RequestContext(request)) 
"""
def show_product(request, pk, template_name="catalogue/detail.html"):
	p = get_object_or_404(Item, id=pk)
	description = p.description
	extra = p.extra
	price = p.price
	name = p.name
	imagename = p.imagename
	form = ProductAddToCartForm()

	if request.method == 'POST':
		postdata = request.POST.copy()
		form = ProductAddToCartForm(request, postdata)
	if form.is_valid():
		cart.add_to_cart(request)
	if request.session.test_cookie_worked():
		request.session.delete_test_cookie()
		url = urlresolvers.reverse('show_cart')
		return HttpResponseRedirect(url)
	else:
		form = ProductAddToCartForm(request=request, label_suffix=':')
		form.fields['pk'].widget.attrs['value'] = pk
		request.session.set_test_cookie()
		return render_to_response("catalogue/detail.html", locals(),context_instance=RequestContext(request)) 
"""