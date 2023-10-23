from rest_framework import serializers
from todolist.models import Post
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_removed', 'created', 'modified']