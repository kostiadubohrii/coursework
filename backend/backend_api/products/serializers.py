from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductLogo

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False, allow_null=True)

    class Meta:
        model = Product 
        fields = ['id', 'name', 'description', 'price', 'oldPrice', 'isApple', 'isActive', 'category', 'review']