from rest_framework import serializers
from .models import Product, ProductImage, ProductLogo, Category, Reviews

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ProductImage
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['id', 'category']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')
    mainImage = serializers.ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    category = CategorySerializer()
    review = ReviewSerializer()

    class Meta:
        model = Product 
        fields = ['id', 
                  'name', 
                  'description', 
                  'price', 
                  'oldPrice', 
                  'isApple', 
                  'isActive', 
                  'category', 
                  'mainImage', 
                  'images', 
                  'review',
                  'created_at',
                  ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = representation['category']['category']
        return representation
