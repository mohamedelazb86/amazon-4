from rest_framework import generics
from .models import Order,Order_Detail
from .serializers import Order_DetailSerializers,OrderSerializers
from django.contrib.auth.models import User

class OrderApi(generics.ListAPIView):
   queryset=Order.objects.all()
   serializer_class=OrderSerializers

   def get_queryset(self):
    user=User.objects.get(username=self.kwargs['username'])
    queryset = super(OrderApi, self).get_queryset()
    queryset = queryset.filter(user=user) # TODO
    return queryset
   
class OrderDetailApi(generics.RetrieveAPIView):
  queryset=Order.objects.all()
  serializer_class=OrderSerializers