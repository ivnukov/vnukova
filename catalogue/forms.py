from django.forms import ModelForm
from django import forms
from catalogue.models import Item, Cart, Email

class CartForm(ModelForm):
    class Meta():
        model = Cart
        fields = ['quantity']


class OrderForm(ModelForm):
    class Meta():
        model = Email
        fields = ['email']
