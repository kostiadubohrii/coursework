MODEL: 
from django.db import models
from users.models import User

# py manage.py makemigrations
# py manage.py migrate 
# py manage.py runserver


class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, blank=False, default=1, on_delete=models.CASCADE)
    orderOn = models.DateField(blank=False, null=True, default=None)

    def __str__(self):
        return "Order ID: %s | Product: %s" % (self.orderId, self.userId)
    
    class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders' 

Serializer:

from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderId', 'userId', 'orderOn']


View: 

from .models import Order
from products.models import Product
from .serializers import OrderSerializer
from orderline.serializers import OrderLineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET', 'POST'])
def orders_list(request, format=None):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def order_detail(request, id, format=None):

    try: 
        order = Order.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def order_and_orderline_spread(request, format=None):
    if request.method == 'POST':
        data = request.data

        order_data = data.get('orderData', {})
        orderLine_data = data.get('orderLineData', {})

        order_serializer = OrderSerializer(data = {
            "userId": order_data.get('userId'),
            "orderOn": order_data.get('orderOn')
        })

        if order_serializer.is_valid():
            order_instance = order_serializer.save()

            orderLine_serializer = OrderLineSerializer(data = {
                "orderId": order_instance.orderId,
                "products": orderLine_data.get('products'),
                "quantity": orderLine_data.get('quantity'),
                "totalPrice": orderLine_data.get('totalPrice'),
            })
            if orderLine_serializer.is_valid():
                orderLine_serializer.save()
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
        return Response({"message": "Order and OrderLine created successfully."}, status=status.HTTP_201_CREATED)
        
        
admin: 

from django.contrib import admin
from orders.models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)








=-------------------


MODEL
from django.db import models
from products.models import Product
from orders.models import Order

# py manage.py makemigrations orderline
# py manage.py migrate orderline
# py manage.py runserver

class OrderLine(models.Model):
    orderLineId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(blank=False, null=True, default=1)
    totalPrice = models.FloatField(blank=False, null=False, default=None)

    def __str__(self):
        return "OrderLine ID: %s" % (self.orderId)
    
    class Meta:
      verbose_name = 'OrderLine'
      verbose_name_plural = 'OrderLines' 


SERIALIZER 

from rest_framework import serializers
from .models import OrderLine
from .models import Product
from django.core.exceptions import ObjectDoesNotExist

class OrderLineSerializer(serializers.ModelSerializer):
    products = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    class Meta:
        model = OrderLine
        fields = ['orderLineId', 'orderId', 'products', 'quantity', 'totalPrice']

    def create_products(self, validated_data):

        product_ids = validated_data.pop("products", [])
        order_line = OrderLine.objects.create(**validated_data)

        for product_id in product_ids:
            try: 
                product = Product.objects.get(id = product_id)
                order_line.products.add(product)
            except ObjectDoesNotExist:
                pass

        return order_line

VIEW 

from .models import OrderLine
from .serializers import OrderLineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def orderLines_list(request, format=None):

    if request.method == 'GET':
        orderLines = OrderLine.objects.all()
        serializer = OrderLineSerializer(orderLines, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def orderLine_detail(request, id, format=None):

    try: 
        orderLine = OrderLine.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderLineSerializer(orderLine)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderLineSerializer(orderLine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        oorderLine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


admin

from django.contrib import admin
from orderline.models import *

class OrderlineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderLine._meta.fields]

    class Meta:
        model = OrderLine
        
admin.site.register(OrderLine, OrderlineAdmin)