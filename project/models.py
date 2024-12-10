# models.py
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True) 

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)  
    product_id = models.IntegerField(null=True, blank=True) 
    quantity = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"Order {self.id}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 

    def __str__(self):
        return self.name
