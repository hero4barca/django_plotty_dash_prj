from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
