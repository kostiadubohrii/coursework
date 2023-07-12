from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        modele = User
        fields = ['id', 'name', 'password']