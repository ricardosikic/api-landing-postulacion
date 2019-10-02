from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='', blank=True, null=True)
    url = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.category_name
