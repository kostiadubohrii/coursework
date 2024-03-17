from .models import User # import User model from models
from .serializers import UserSerializer # import serializer of the User model, so api can be set
from rest_framework.decorators import api_view # import decorators, so GET and POST request can be applied by frontend 
from rest_framework.response import Response # import respons
from rest_framework import status # import status of the erors 

@api_view(['GET', 'POST'])
def users_list(request, format=None):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PATCH'])
def user_detail(request, id, format=None):

    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({
                "status": "failure",
                "message": f"User with id: {id} does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)