from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import activate
from .models import Product_type,Products
from .forms import Products_forms

def new_product(request):
    if request.method=='POST':
        form = Products_forms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('getall')
    form = Products_forms()
    return render(request, 'add.html', {'form':form})

def view_allproducts(request):
    if request.method=='GET':
        products = Products.objects.all()
        return render(request, 'list.html', {'products':products})
    return redirect('getall')

def view_product(request, name:str):
    products = Products.objects.filter(name = name, available=True)
    return render(request, 'getproduct_list.html', {'products':products})

def update(request, name:str):
    products = Products.objects.get(name = name, available=True)
    if request.method == 'POST':
        form = Products_forms(data=request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('getall')
    form = Products_forms()
    return render(request, 'update_pro.html', {'form':form})
    
def delete(request, name:str):
    products = Products.objects.get(name=name, available=True)
    if products: 
        products.delete()
        return redirect('getall')
    form = Products_forms(instance=products)
    return render(request, 'getproduct_list.html', {'form':form})

   