from rest_framework import serializers
from .models import OrderLine, OrderLineProduct
from products.models import Product


class OrderLineProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField()

    class Meta:
        model = OrderLineProduct
        fields = ["product", "quantity"]

class OrderLineSerializer(serializers.ModelSerializer):
    products = OrderLineProductSerializer(many=True, source="orderlineproduct_set")
    class Meta:
        model = OrderLine
        fields = [
            'orderLineId', 
            'orderId', 
            'products', 
            'totalPrice',
            'created_at'
            ]
    
    def create(self, validated_data):
        products = validated_data.pop("orderlineproduct_set", [])
        orderline = OrderLine.objects.create(**validated_data)

        for product in products:
            product_id = product.get('product')
            if product_id is not None:
                try:
                    quantity = product.get('quantity')
                    product = Product.objects.get(id=product_id)
                    
                    OrderLineProduct.objects.create(orderline=orderline, product=product, quantity=quantity)
                except Product.DoesNotExist:
                    pass 

        return orderline
    

    