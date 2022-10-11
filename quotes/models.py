from django.db import models
from django.contrib.auth.models import AbstractUser



class Quote(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.username
