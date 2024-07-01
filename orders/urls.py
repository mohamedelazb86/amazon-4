from django.urls import path
from .views import order_list,checkout
from .api import OrderApi,OrderDetailApi

urlpatterns = [
    path('',order_list),
    path('checkout',checkout),

    #api

    path('<str:username>/api',OrderApi.as_view()),
    path('<str:urename>/<int:pk>',OrderDetailApi.as_view()),
]
