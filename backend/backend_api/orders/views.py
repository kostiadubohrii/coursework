from .models import Order
from products.models import Product
from users.models import User
from .serializers import OrderSerializer
from orderline.serializers import OrderLineSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime


@api_view(['GET', 'POST'])
def orders_list(request, format=None):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else: 
            return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def order_detail(request, id, format=None):

    try: 
        order = Order.objects.get(pk=id)
    except:
        return Response({
            "status": "failure",
            "message":  f"Order with id: {id} does not exist"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
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
        order.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def order_and_orderline_spread(request, format=None):
    if request.method == 'POST':
        data = request.data

        order_data = data.get('orderData', {})
        order_line_data = data.get('orderLineData', {})
        user_id = order_data['userId']
        order_on = order_data['orderOn']

        try: 
            user = User.objects.get(pk=user_id)
        except:
            return Response({
                "status": "failure",
                "message": f"User with id - {user_id} does not exist"
            }, status=status.HTTP_400_BAD_REQUEST)

        order_serializer = OrderSerializer(data = {
            "userId": order_data.get('userId'),
            "orderOn": order_data.get('orderOn')
        })
        products_all = Product.objects.all()

        product_ordered = order_line_data.get('products')
        
        internal_product_price = 0

        for external in product_ordered: 
            for internal in products_all:
                if external.get('product') == internal.id:
                    internal_product_price += internal.price * external.get('quantity')
        

        error_message = {}

        def format_check(date, fmt):
            try: 
                datetime.strptime(date, fmt)
            except: 
                return False

            else: return True
            
        if format_check(order_on, '%Y-%m-%d'):
            if datetime.strptime(order_on, "%Y-%m-%d") < datetime.now():
                return Response({
                    "status": "failure",
                    "message": "Past date time"
                },  status=status.HTTP_400_BAD_REQUEST)
        
        if internal_product_price != float(order_line_data.get('totalPrice')):
            return Response({
                    "status": "failure",
                    "message": f"Incorrect total price. Must be {internal_product_price}"
                },  status=status.HTTP_400_BAD_REQUEST)

        
        if order_serializer.is_valid():
            if not len(error_message):
                order_instance = order_serializer.save()

                orderLine_serializer = OrderLineSerializer(data = {
                    "orderId": order_instance.orderId,
                    "products": order_line_data.get('products'),
                    "totalPrice": order_line_data.get('totalPrice'),
                })


                if orderLine_serializer.is_valid():
                    orderLine_serializer.save()

                else:
                    order_instance.delete()
                    return Response({
                        "status": "failure",
                        "message": orderLine_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(error_message,  status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "status": "failure",
                "message": order_serializer.errors
            },  status=status.HTTP_400_BAD_REQUEST)
        
    
    return Response({
        "status": "success",
        "message": "Order has been created"
    }, status=status.HTTP_201_CREATED)
        