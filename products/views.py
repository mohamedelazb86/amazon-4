from django.shortcuts import render
from .models import Product,Brand
from django.views.generic import ListView,DetailView

class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=25

class product_detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

