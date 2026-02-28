from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=13,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    email=models.EmailField(unique=True)
    bio=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username
