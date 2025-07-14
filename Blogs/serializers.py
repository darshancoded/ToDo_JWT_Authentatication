from .models import Blog
from rest_framework import serializers
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields = ['id','title','content','author','created_at','status']
        read_only_fields = ['id','author','created_at']
        
        