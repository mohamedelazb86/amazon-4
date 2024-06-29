from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image_user')
    code=models.CharField(max_length=50,default=generate_code)



    def __str__(self):
        return str(self.user)

# create singals
@receiver(post_save,sender=User)    
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )

ADDRESS_TYPE=[
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others'),

    ]
class Address(models.Model):
    user=models.ForeignKey(User,related_name='address_user',on_delete=models.CASCADE)
    address_type=models.CharField(max_length=75,choices=ADDRESS_TYPE)
    address=models.TextField(max_length=500)

    def __str__(self):
        return str(self.user)

