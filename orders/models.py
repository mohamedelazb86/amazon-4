from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from accounts.models import Address
from products.models import Product

ORDER_TYPE=[
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ]
class Order(models.Model):
    user=models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=75,choices=ORDER_TYPE)
    code=models.CharField(max_length=50,default=generate_code)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    copoun=models.ForeignKey('Copoun',related_name='order_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total=models.FloatField(null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)




class Order_Detail(models.Model):
    order=models.ForeignKey(Order,related_name='detail_order',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='detatil_product',on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total=models.FloatField(null=True,blank=True)


CART_TYPE=[
    ('Complete','Complete'),
    ('Inprogress','Inprogress'),
    
    ]
class Cart(models.Model):
    user=models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=75,choices=CART_TYPE)
    
    copoun=models.ForeignKey('Copoun',related_name='cart_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    
    total_with_copoun=models.FloatField(null=True,blank=True)

class Cart_Detail(models.Model):
    cart=models.ForeignKey(Order,related_name='detail_cart',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='detatil_productcart',on_delete=models.CASCADE)
    quantity=models.FloatField(default=1)
   
    total=models.FloatField(null=True,blank=True)



class Copoun(models.Model):
    code=models.CharField(max_length=120)
    startdate=models.DateField(default=timezone.now)
    enddate=models.DateField(null=True,blank=True)
    quantity=models.IntegerField()
    discount=models.FloatField()

    def save(self,*args,**kwargs):
        week=timezone.timedelta(days=7)
        self.enddate=self.startdate + week
        super(Copoun,self).save(*args,**kwargs)

    
