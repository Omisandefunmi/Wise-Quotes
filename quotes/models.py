from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Quote(models.Model):
    SOURCE_CHOICE = (
        ("AGQ", "Api_generated"),
        ("UGQ", "User_generated")
    )
    message = models.TextField(unique=True)
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=3, choices=SOURCE_CHOICE)


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.username
