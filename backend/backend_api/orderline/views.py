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