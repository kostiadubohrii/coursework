from .models import User # import User model from models
from .serializers import UserSerializer # import serializer of the User model, so api can be set
from rest_framework.decorators import api_view # import decorators, so GET and POST request can be applied by frontend 
from rest_framework.response import Response # import respons
from rest_framework import status # import status of the erors 

@api_view(['GET', 'POST'])
def users_list(request, format=None):

    if request.method == 'GET':
        drinks = User.objects.all()
        serializer = UserSerializer(drinks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):

    try:
        drink = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)