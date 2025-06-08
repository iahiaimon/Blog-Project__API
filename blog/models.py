from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}--{self.email}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    username = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}--{self.username}"
