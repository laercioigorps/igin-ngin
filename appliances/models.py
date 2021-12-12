from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Appliance(models.Model):
    model = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
