from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to="postCovers", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=15)
    content = models.TextField()


# O que é o author?
class Author:
    pass
