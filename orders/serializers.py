from rest_framework import serializers
from .models import Order,Order_Detail
from django.contrib.auth.models import User



class Order_DetailSerializers(serializers.ModelSerializer):
    order=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    
    class Meta:
        model=Order_Detail
        fields='__all__'


class OrderSerializers(serializers.ModelSerializer):
    
    order_detail=Order_DetailSerializers(source='detail_order',many=True)
    class Meta:
        model=Order
        fields='__all__'

    