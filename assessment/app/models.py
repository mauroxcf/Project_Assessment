from django.db import models

# Create your models here.
class Users(models.Model):
    idUser = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gov_id = models.IntegerField()
    email = models.CharField(max_length=60)
    company = models.CharField(max_length=45)

class Order(models.Model):
    idOrder = models.IntegerField(primary_key=True)
    date = models.DateField()
    total = models.FloatField()
    subtotal = models.FloatField()
    taxes = models.FloatField()
    paid = models.FloatField()
    id_user = models.ForeignKey(Users, on_delete = models.CASCADE)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    cost = models.FloatField()

class payments(models.Model):
    idpayment = models.IntegerField(primary_key=True)
    types = models.CharField(max_length=45)
    date = models.DateField()
    txn_id = models.IntegerField()
    total = models.FloatField()
    status = models.CharField(max_length=45)
    id_order = models.ForeignKey(Order, on_delete = models.CASCADE)
