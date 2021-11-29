from rest_framework import viewsets, status
from .models import Shop, Order
from .serializers import ShopSerializers, OrderSerializers
from rest_framework.response import Response
from user_order.producer import publish

class ShopViewSets(viewsets.ViewSet):
    def list(self, request): #/api/shop
        shops = Shop.objects.all()
        serializers = ShopSerializers(shops, many=True)
        return Response(serializers.data)

    def create(self, request): #/api/shop
        serializers = ShopSerializers(data=request.data)
        serializers.is_valid(raise_exception=True) # 유효한지 체크 유효하지않으면 예외 처리
        serializers.save()
        publish('shop_created', serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        serializers = ShopSerializers(shop)
        return Response(serializers.data)

    def update(self, request, pk=None): #api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        serializers = ShopSerializers(instance=shop, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        publish('shop_updated', serializers.data)
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        shop.delete()
        publish('shop_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSets(viewsets.ViewSet):
    def list(self, request): #/api/order
        orders = Order.objects.all()
        serializers = OrderSerializers(orders, many=True)
        return Response(serializers.data)

    def create(self, request): #/api/order
        serializers = OrderSerializers(data=request.data)
        serializers.is_valid(raise_exception=True) # 유효한지 체크 유효하지않으면 예외 처리
        serializers.save()
        publish('order_created', serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #api/order/<str:idx>
        order = Order.objects.get(id=pk)
        serializers = OrderSerializers(order)
        return Response(serializers.data)

    def update(self, request, pk=None): #api/order/<str:idx>
        order = Order.objects.get(id=pk)
        serializers = OrderSerializers(instance=order, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        publish('order_updated', serializers.data)
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #api/order/<str:idx>
        order = Order.objects.get(id=pk)
        order.delete()
        publish('order_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)