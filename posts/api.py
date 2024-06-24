from .serializers import PostlistSerailizers,PostDetailSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .mypaginations import Mypaginations



class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostlistSerailizers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]
    pagination_class=Mypaginations


    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['publish_date',]

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers
    permission_classes = [IsAuthenticated]