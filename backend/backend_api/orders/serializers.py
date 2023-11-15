from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    orderOn = serializers.DateField(
        format='%Y-%m-%d',
        input_formats=['%Y-%m-%d', 'iso-8601']
    )
    class Meta:
        model = Order
        fields = ['orderId', 'userId', 'orderOn']