from django.db import models

# Create your models here.

class Laptop(models.Model):
    password = models.CharField(max_length=50)
    re_password=models.CharField(max_length=50)
    laptop=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    ram=models.IntegerField()
    youtube=models.BooleanField()