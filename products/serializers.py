from rest_framework import serializers
from .models import Product,Brand,ProductImage


class ProductImageSerailizers(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    class Meta:
        model=ProductImage
        fields='__all__'

class Product_ListSerilizers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    images=ProductImageSerailizers(source='image_product',many=True)
    class Meta:
        model=Product
        fields='__all__'

class Product_DetailSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    images=ProductImageSerailizers(source='image_product',many=True)
    class Meta:
        model=Product
        fields='__all__'



class Brand_listSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'


class Brand_detailSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'