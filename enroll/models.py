from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)













