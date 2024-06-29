from django.urls import path
from .views import signup,activate_code,dasbord

urlpatterns = [
    path('signup',signup),
    path('<str:username>/activate',activate_code),
    path('dasbord',dasbord),
]
