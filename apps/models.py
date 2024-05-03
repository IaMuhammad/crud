from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
