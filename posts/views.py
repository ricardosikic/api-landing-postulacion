from django.shortcuts import render
from .models import Article, Category
# from rest_framework import generics cambiado x viewsets
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer




# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
