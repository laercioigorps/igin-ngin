from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
