from rest_framework import serializers
from readwrite.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'pub_date','content', 'words', 'is_top')