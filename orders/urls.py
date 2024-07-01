from django.urls import path
from .views import order_list,checkout,add_to_cart
from .api import OrderApi,OrderDetailApi,Apply_Copoun

urlpatterns = [
    path('',order_list),
    path('checkout',checkout),
    path('add_to_cart',add_to_cart),

    #api

    path('<str:username>/api',OrderApi.as_view()),
    path('<str:urename>/<int:pk>',OrderDetailApi.as_view()),
    path('api/<str:username>/apply_copoun',Apply_Copoun.as_view()),
]
