from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Order,Cart,Cart_Detail,Copoun
from django.shortcuts import  get_object_or_404
from settings.models import Delivery_fee
import datetime
from products.models import Product



def order_list(request):
   

    orders=Order.objects.filter(user=request.user)

    context={
        'orders':orders
    }
    
    return render(request,'orders/order_list.html',context)


def checkout(request):
    
    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail=Cart_Detail.objects.filter(cart=cart)
    delivery_fee=Delivery_fee.objects.last().fee


    if request.method=='POST':
        copoun_code=request.POST['copoun_id']
        #copoun=Copoun.objects.get(code=copoun_code)
        copoun=get_object_or_404(Copoun,code=copoun_code)
        if copoun and copoun.quantity > 0:
            datenow=datetime.datetime.today().date()
            if datenow >= copoun.startdate and datenow <= copoun.enddate :
                copoun_value=cart.cart_total /100 * copoun.discount
                subtotal=cart.cart_total - copoun_value

                total = subtotal + delivery_fee -copoun_value

                cart.copoun = copoun
                cart.total_with_copoun =total
                cart.save()

                copoun.quantity -= 1
                copoun.save()
                
                context={
                        'cart_detail':cart_detail,
                        'subtotal':subtotal,
                        'discount':copoun_value,
                        'delivery_fee':delivery_fee,
                        'total':total,

                }

                return render(request,'orders/checkout.html',context)

                



    subtotal=cart.cart_total
    discount=0

    total=subtotal+delivery_fee

   


    context={
        'cart_detail':cart_detail,
        'subtotal':subtotal,
        'discount':discount,
        'delivery_fee':delivery_fee,
        'total':total,

    }
    
    return render(request,'orders/checkout.html',context)


def add_to_cart(request):
    product=Product.objects.get(id=request.POST['product_id'])
    quantity=int(request.POST['quantity'])

    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail,created=Cart_Detail.objects.get_or_create(cart=cart,product=product)

    cart_detail.quantity=quantity
    cart_detail.total=cart_detail.quantity * product.price
    cart_detail.save()
    
    return redirect(f'/products/{product.slug}')


   