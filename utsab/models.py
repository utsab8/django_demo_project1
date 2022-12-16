from django.db import models


# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20)
    price = models.CharField(max_length=10)


    def __str__(self):
        return self.name 