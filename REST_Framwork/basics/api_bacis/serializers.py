from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Article

# Model Serializer
class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = "__all__"

# Functions based serializer view --> go to apps views

















'''
class ArticleSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    date=serializers.DateTimeField()
    
    def create(self,validated_data):
        return Article.objects.create(validated_data)
    
    
    def update(self,validated_data,instance):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.email=validated_data.get('email',instance.email)
        instance.date=validated_data.get('date',instance.date)
        instance.save()
        return instance
'''