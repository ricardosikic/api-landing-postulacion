from rest_framework import serializers
from .models import Article, Category
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):

    class Meta: 
        fields = ('id', 'author', 'title', 'description', 'content', 'category', 'url', 'photo', 'created_at', 'updated_at')
        model = Article



class CategorySerializer(serializers.ModelSerializer):

    class Meta: 
        fields = ('id', 'category_name')
        model = Category


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'username',)
        model = get_user_model()