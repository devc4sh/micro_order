from rest_framework import serializers
from user_order.models import Shop, Order


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
