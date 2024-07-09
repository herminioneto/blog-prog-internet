from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=15, verbose_name="Nome de usuário", unique=True
    )
