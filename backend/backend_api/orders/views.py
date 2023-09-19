from .models import Order
from .serializers import OrderSerializer
from orderline.serializers import OrderLineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
        order_line_data = data.get('orderLineData', {})

        order_serializer = OrderSerializer(data = {
            "userId": order_data.get('userId'),
            "orderOn": order_data.get('orderOn')
        })

        if order_serializer.is_valid():
            order_instance = order_serializer.save()

            orderLine_serializer = OrderLineSerializer(data = {
                "orderId": order_instance.orderId,
                "product": order_line_data.get('product'),
                "quantity": order_line_data.get('quantity'),
                "totalPrice": order_line_data.get('totalPrice'),
            })


            if orderLine_serializer.is_valid():
                orderLine_serializer.save()
            else:
                order_instance.delete()
                return Response(orderLine_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
        return Response({"message": "Order and OrderLine created successfully."}, status=status.HTTP_201_CREATED)
        
        
