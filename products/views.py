from django.shortcuts import render,redirect
from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView

class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=25

class product_detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:5]
        context["myimages"] =ProductImage.objects.filter(product=self.get_object())
        context["related"] =Product.objects.filter(brand=self.get_object().brand)
        return context
    

def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    user=request.user
    rate=request.POST['rating']
    content=request.POST['content']

    Review.objects.create(
        product=product,
        user=user,
        rate=rate,
        content=content

    )

    return redirect(f'/products/{slug}')
    
    



