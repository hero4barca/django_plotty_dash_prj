from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    stock_qty = models.IntegerField(default=1)

    @property
    def availability(self):
        if self.stock_qty > 0:
            return True
        else:
            return False
