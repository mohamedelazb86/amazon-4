from .serializers import PostlistSerailizers,PostDetailSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post

class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostlistSerailizers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers
    permission_classes = [IsAuthenticated]