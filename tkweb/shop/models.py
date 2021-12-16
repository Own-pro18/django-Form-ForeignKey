from django.db import models
from django.utils.timezone import get_current_timezone
from datetime import datetime

class Product_type(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    brand_n = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.brand_n}'

class Products(models.Model):
    category = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=500, null=False)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name="stock")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
