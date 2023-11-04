from django.db import models

class EquipmentCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True,max_length=45)
    date_created = models.DateField(auto_now=True)
    
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(EquipmentCategory,on_delete=models.CASCADE)
    product_name = models.CharField(unique=True,max_length=20)
    unit_price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    unit_measure = models.CharField(unique=True,max_length=10)
    date_updated = models.DateField(auto_now=True)

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    transaction_type = models.CharField(unique=True,max_length=10)
    stock_taken = models.IntegerField(default=0)
    transaction_amount = models.IntegerField(default=0)
    transaction_date = models.DateField(auto_now=True)
    

