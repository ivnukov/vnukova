# -*- coding: utf-8 -*-

from catalogue.models import Item, Cart
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.core.paginator import Paginator
from .forms import CartForm, OrderForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.mail import mail_admins
import random

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id 

def main(request):
    item = Item.objects.all()
    cart_id = _cart_id(request)
    return render(request, 'catalogue/catalogue.html', {'item': item})

def list_view(request, section_id):
    if section_id == "A":
        item = Item.objects.all()
    else:
        item = Item.objects.filter(section = section_id)
    count = len(item)
    return render(request, 'catalogue/list_view.html', {'item': item, 'count':count})


def product(request, pk):
    cart_form = CartForm
    args = {'cart_add_form': cart_form,	'item': Item.objects.get(id=pk)}
    args.update(csrf(request))
    rec_items = Item.objects.all()
    args['randomitem'] = [
        Item.objects.get(id = random.randint(1,len(rec_items)-1)),
        Item.objects.get(id = random.randint(1,len(rec_items)-1)),
        Item.objects.get(id = random.randint(1,len(rec_items)-1))]
    return render_to_response('catalogue/detail.html', args)

def add_to_cart(request, id):
    product_id = id
    p = Item.objects.get(id=id)
    if request.method == 'POST':
        form = CartForm(request.POST)
        product_in_cart = False
        current_cart = Cart.objects.filter(owner = request.session[CART_ID_SESSION_KEY])
        if form.is_valid():
            for product in current_cart:

                if product.product.id == p.id:
                    product.increase_quantity(request.POST['quantity'])
                    product_in_cart = True
            if not product_in_cart:
                cart = form.save(commit=False)
                cart.owner = _cart_id(request)
                cart.product = Item.objects.get(id=id)
                form.save()
    return redirect('/catalogue/detail/%s/' % product_id)

def cart(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['email']=OrderForm
    args.update(csrf(request))
    args['cart'] = Cart.objects.filter(owner=request.session[CART_ID_SESSION_KEY])
    args['totalcost'] = 0
    for each in args['cart']:
        args['totalcost']+=int(each.cost())
    return render_to_response('cart/cart.html', args)


def del_from_cart(request, id):
    Cart.objects.get(id=id).delete()
    return redirect('/catalogue/cart/')

def increase(request, id):
    Cart.objects.get(id = id).increase_quantity(1)
    return redirect('/catalogue/cart/')

def decrease(request, id):
    item = Cart.objects.get(id = id)
    if item.quantity == 1:
        item.delete()
    else:    
        item.increase_quantity(-1)
    return redirect('/catalogue/cart/')    

def order(request):
    if request.POST:
        form=OrderForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            mail_admins(u'Оформлен заказ!', 'На сайте оставлен заказ!')
            return redirect('/')
        else:
            return redirect('/catalogue/cart/')