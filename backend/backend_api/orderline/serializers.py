from rest_framework import serializers
from .models import OrderLine

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['orderLineId', 'orderId', 'product', 'quantity', 'totalPrice']

    