from django.shortcuts import render,redirect
from django.core.mail import send_mail

from .forms import SignupForm,ActivateForm
from .models import Profile
from django.contrib.auth.models import User
from products.models import Product,Brand



def signup(request):
    
    '''
            - create new user
            - send email to this user
            - stop activte user
            - rediect to activate html
    '''
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)  
            user.is_active=False
            form.save()  # create new user and creat profile
            
            
            
             # send email

            profile=Profile.objects.get(user__username=username)
            send_mail(
                "Activate code",
                f"welcome mr {username}\n pls user this code {profile.code}",
                "r_mido99@yahoo.com",
                [email],
                fail_silently=False,
                )
            return redirect(f'/accounts/{username}/activate')
            

    else:
        form=SignupForm()
    return render(request,'accounts/signup.html',{'form':form})


def activate_code(request,username):
   
    '''
        - comparte this code with code for this user
        - active user
        - save user and profile models
        - redirect login html


    '''
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code=''

                user=User.objects.get(username=username)
                user.is_active=True

                user.save()
                profile.save()

                return redirect('accounts/login')

    else:
        form=ActivateForm()
    return render(request,'accounts/activate.html',{'form':form})


def dasbord(request):
    users=User.objects.all().count()
    new_product=Product.objects.filter(flag='New').count()
    brands=Brand.objects.all().count()

    context={
        'user':users,
        'mynew':new_product,
        'mybrand':brands,
        

    }
    return render(request,'accounts/dasbord.html',context)
