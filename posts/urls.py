from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import ArticleList, ArticleDetail, CategoryList, UserDetail, UserList
from .views import ArticleViewSet, CategoryViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('categories', CategoryViewSet)
router.register('', ArticleViewSet, base_name='articles')

urlpatterns = router.urls

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>', ArticleDetail.as_view()),
#     path('', ArticleList.as_view()),
#     path('categories', CategoryList.as_view()),
# ]