from django.shortcuts import render
from .models import Article, Category
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer, CategorySerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer