from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    url = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
