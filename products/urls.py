from django.urls import path
from .views import product_detail,Product_list

urlpatterns = [
    path('',Product_list.as_view()),
    path('<slug:slug>',product_detail.as_view()),
]
