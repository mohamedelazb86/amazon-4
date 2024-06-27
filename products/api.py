from .serializers import Product_DetailSerializers,Product_ListSerilizers,Brand_detailSerailizers,Brand_listSerailizers
from rest_framework import generics
from .models import Product,Brand
from posts.mypaginations import Mypaginations


class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Product_ListSerilizers
    pagination_class=Mypaginations

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=Product_DetailSerializers




class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=Brand_listSerailizers

class BrandDetailApi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=Brand_detailSerailizers