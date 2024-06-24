from rest_framework import serializers
from .models import Post


class PostlistSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class PostDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        