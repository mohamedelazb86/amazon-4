from django.urls import path
from .views import post_detail,post_list,update_post

urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('<slug:slug>/update',update_post),
]
