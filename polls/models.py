from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Table(models.Model):
    tb_no = models.IntegerField(primary_key=True)
    Qr_no = models.CharField(max_length=20)
    status = models.BooleanField()

class food_item(models.Model):
    food_id = models.CharField(max_length=10, primary_key=True)
    food_name = models.CharField(max_length=20)
    catagory = models.CharField(max_length=20)
    price = models.IntegerField()
    avg_review = models.IntegerField()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    tb_no = models.ForeignKey(Table, null=True, on_delete=models.CASCADE)
    date_time = models.DateField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    phone_no = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    bill_no = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    exit_status = models.BooleanField(blank=True, null=True)

class Order_food_mapping(models.Model):
    order_id = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    food_id = models.ForeignKey(food_item, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_price = models.IntegerField(blank=True, null=True)
    modification = models.CharField(max_length=100, blank=True, null=True)


