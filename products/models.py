from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
]
class Product(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=120,choices=FLAG_TYPE)
    price=models.FloatField()
    image=models.ImageField(upload_to='photo_product')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=5000)
    descriptions=models.TextField(max_length=50000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    quantity=models.FloatField()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,related_name='image_product',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)

class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    content=models.TextField(max_length=1500)
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user}---{self.product}'



class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='image_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name


