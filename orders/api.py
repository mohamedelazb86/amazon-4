from rest_framework import generics
from .models import Order,Order_Detail,Copoun,Cart,Cart_Detail
from .serializers import Order_DetailSerializers,OrderSerializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import datetime
from settings.models import Delivery_fee
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Address
from products.models import Product





class OrderApi(generics.ListAPIView):
   queryset=Order.objects.all()
   serializer_class=OrderSerializers

   def get_queryset(self):
    user=User.objects.get(username=self.kwargs['username'])
    queryset = super(OrderApi, self).get_queryset()
    queryset = queryset.filter(user=user) # TODO
    return queryset
   


   
class OrderDetailApi(generics.RetrieveAPIView):
  queryset=Order.objects.all()
  serializer_class=OrderSerializers



class Apply_Copoun(generics.GenericAPIView):
  def post(self,request,*args,**kwargs):
    user=User.objects.get(username=self.kwargs['username'])
    cart=Cart.objects.get(user=user,status='Inprogress')
    copoun_code=request.data['copoun_code']
    #copoun=Copoun.objects.get(code=copoun_code)
    copoun=get_object_or_404(Copoun,code=copoun_code)
    if copoun and copoun.quantity > 0:
      today=datetime.datetime.today().date()
      if today >= copoun.startdate and today <= copoun.enddate:
        copoun_value=cart.cart_total /100 * copoun.discount
        delivery_fee=Delivery_fee.objects.last().fee
        subtotal= cart.cart_total + delivery_fee - copoun_value

        cart.copoun=copoun
        cart.total_with_copoun = subtotal
        cart.save()

        copoun.quantity -=1
        copoun.save()

        return  Response({'message':'ok appply copoun succefully'},status=status.HTTP_200_OK)
      else:
        return Response({'message':'sorry this copoun_code expired'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'this copoun not found'},status=status.HTTP_404_NOT_FOUND)
  

class Create_Order(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
      user=User.objects.get(username=self.kwargs['username'])
      cart=Cart.objects.get(user=user,status='Inprogress')
      cart_detail=Cart_Detail.objects.filter(cart=cart)
      address=request.data['address_id']
      user_address=Address.objects.get(id=address)


      # cart:order
      new_order=Order.objects.create(
        user=user,
        code=request.data['payment_code'],
        status='Recieved',
        delivery_address=user_address,
        copoun=cart.copoun,
        total_with_copoun=cart.total_with_copoun,
        total=cart.cart_total
      )
      # cart_detail  : order_detail
      for item in cart_detail:
        product=Product.objects.get(id=item.product.id)
        Order_Detail.objects.create(
          order=new_order,
          product=product,
          quantity=item.quantity,
          price=product.price,
          total=round(item.quantity * item.product.price,2),
        )
        # decrese product
        product.quantity -=item.quantity
        product.save()

      cart.status='Complete'
      cart.save()

      return Response({'message':'ok create order is sucssefully'},status=status.HTTP_200_OK)
    
    

