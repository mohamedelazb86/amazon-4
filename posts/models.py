from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    user=models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120,verbose_name=_('title'))
    content=models.TextField(max_length=2000)
    category= models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(upload_to='photo_post')
    draft=models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True)
    publish_date=models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.CharField(max_length=120)
    post=models.ForeignKey(Post,related_name='review_post',on_delete=models.SET_NULL,null=True,blank=True)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    content=models.TextField(max_length=500)
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)


