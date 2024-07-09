from django.contrib.auth.models import User
from django.db import models

# O ideal seria o author estender de AbstractUser,
# mas isso deve ser feito ao início do app


# Declarando o User como Proxy Model
# https://docs.djangoproject.com/en/5.0/topics/db/models/#proxy-models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to="postCovers", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=15)
    content = models.TextField()
    owner = models.ForeignKey(Author, on_delete=models.CASCADE)
