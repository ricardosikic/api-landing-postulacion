from django.urls import path

from .views import ArticleList, ArticleDetail, CategoryList

urlpatterns = [
    path('<int:pk>', ArticleDetail.as_view()),
    path('', ArticleList.as_view()),
    path('categories', CategoryList.as_view()),
]