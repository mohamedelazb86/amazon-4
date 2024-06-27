from django.urls import path
from .views import product_detail,Product_list,add_review,Brand_Detail,Brand_List
from .api import ProductDetailApi,ProductListApi,BrandDetailApi,BrandListApi


urlpatterns = [

    path('brands',Brand_List.as_view()),
    path('<slug:slug>/brands',Brand_Detail.as_view()),


    path('',Product_list.as_view()),
    path('<slug:slug>',product_detail.as_view()),
    path('<slug:slug>/add_review',add_review),

    # api
     path('api/productlist',ProductListApi.as_view()),
     path('api/productdetail/<int:pk>',ProductDetailApi.as_view()),

     path('api/brandlist',BrandListApi.as_view()),
     path('api/brandetail/<int:pk>',BrandDetailApi.as_view()),
]
