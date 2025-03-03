from django.db import models

# Create your models here.

class product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice=models.DecimalField(max_digits=10, decimal_places=2)
    
    