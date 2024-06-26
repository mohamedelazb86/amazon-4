from django.shortcuts import render
from .models import Product,Brand
from django.views.generic import ListView,DetailView

class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'

class product_detail(DetailView):
    model=Product
    template_name='product/product_detail.html'

