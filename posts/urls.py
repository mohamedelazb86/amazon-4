from django.urls import path
from .views import post_detail,post_list,update_post,delete_post
from .api import PostListApi,PostDetailApi,PostUpdateApi

urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('<slug:slug>/update',update_post),
    path('<slug:slug>/delete/delete',delete_post),

    # api

    path('api/postlist',PostListApi.as_view()),
    path('api/postdetail/<int:pk>',PostDetailApi.as_view()),
    path('api/postupdate/<int:pk>/update',PostUpdateApi.as_view()),
]
