from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/product/', new_product, name='addproduct'),
    path('view/all/products', view_allproducts, name='getall'),
    path('view/products/<name>', view_product, name='getone'),
    path('update/products/<name>', update, name='update_product'),
    path('delete/products/<name>', delete, name='delete_product'),
]
