from django.shortcuts import render
from products.models import Brand,Product,Review
from django.db.models.aggregates import Count
# Create your views here.

def home(request):
    brands=Brand.objects.all().annotate(product_count=Count('product_brand'))[:10]
    sale_product=Product.objects.filter(flag='Sale')[:10]
    new_product=Product.objects.filter(flag='New')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]
    reviews=Review.objects.all()

    context={
        'brands':brands,
        'sale_product':sale_product,
        'new_product':sale_product,
        'feature_product':feature_product,
        'reviews':reviews,
    }

    return render(request,'settings/home.html',context)
