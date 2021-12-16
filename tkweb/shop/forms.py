from collections import namedtuple
from django import forms
from django.db import models
from django.db.models import fields
from .models import Products, Product_type, Brand

class Product_type_form(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Product_type
        fields = ('name',)

class Brand_form(forms.ModelForm):
    brand_n = forms.CharField(required=True)

    class Meta:
        model = Brand
        fields = ('brand_n',)

class Products_forms(forms.ModelForm):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    price = forms.DecimalField(required=True)
    stock = forms.IntegerField(required=True)

    class Meta:
        model = Products
        # fields = ('name','description','price','stock')
        fields = '__all__'