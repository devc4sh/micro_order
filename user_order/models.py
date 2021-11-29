from django.db import models

class Shop(models.Model):
    shop_name= models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) #shop이 delete 되면 맞는 pk 값도 Delete
    order_data = models.DateTimeField('date ordered', auto_now_add=True)
    address = models.CharField(max_length=40)
    delivery_finish = models.BooleanField(default=0)