from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.DecimalField(decimal_places=2, max_digits=5 ,null=False)
