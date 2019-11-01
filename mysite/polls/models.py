from django.db import models

# Create your models here.

class Demo(models.Model):
    name = models.CharField(max_length=35)
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=35)
    birthday = models.DateTimeField(null=True)
