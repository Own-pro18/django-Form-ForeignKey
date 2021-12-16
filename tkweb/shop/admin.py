from django.contrib import admin
from .models import Brand, Product_type, Products

admin.site.register(Products)
admin.site.register(Product_type)
admin.site.register(Brand)