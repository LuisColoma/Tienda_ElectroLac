from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200, default="") 
    last_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=254, default = "")
    edad = models.PositiveIntegerField(default=18)
    photo = models.ImageField(blank = True, null = True)
    type = models.CharField(max_length=10, default="")