from django.db import models

# Create your models here.
class Employees(models.Model):
    empName = models.CharField(max_length=100)
    empAddress = models.TextField()
    