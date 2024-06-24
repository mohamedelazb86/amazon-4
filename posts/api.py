from .serializers import PostlistSerailizers,PostDetailSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend

class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostlistSerailizers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers
    permission_classes = [IsAuthenticated]