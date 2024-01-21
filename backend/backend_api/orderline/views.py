from .models import OrderLine, OrderLineProduct
from .serializers import OrderLineSerializer
from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from datetime import datetime
from collections import defaultdict
import calendar

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

def product_statistics(request):
    if request.method == "GET":
        orderline_products = OrderLineProduct.objects.all()
        products = Product.objects.all()

        temp = {}

        def setRevenueSoldDict(month, quantity, price):
            sold = [0,0,0,0,0,0,0,0,0,0,0,0]
            sold[month] = quantity

            revenue = [0,0,0,0,0,0,0,0,0,0,0,0]
            revenue[month] = quantity * price

            return {
                "revenue": revenue,
                "sold": sold
            }

        for order in orderline_products: 
            orderItemId = order.product.pk 
            order_date_year = order.created_at.strftime("%d/%m/%Y")[6:10]
            order_date_month = int(order.created_at.strftime("%d/%m/%Y")[3:5]) - 1
            product_price = Product.objects.get(pk=orderItemId).price

            if orderItemId in temp:
                if order_date_year in temp[orderItemId]:
                    temp[orderItemId][order_date_year]["sold"][order_date_month] += order.quantity
                    temp[orderItemId][order_date_year]["revenue"][order_date_month] += order.quantity * product_price

                else:
                    temp[orderItemId][order_date_year] = setRevenueSoldDict(order_date_month, order.quantity, product_price)

            else:
                temp[orderItemId] = {
                    "id": orderItemId,
                    "name": order.product.name,
                    order_date_year: setRevenueSoldDict(order_date_month, order.quantity, product_price)
                }
        
        data = []
        for item in temp:
            data.append(temp[item])

        response = {
            "status": "success",
            "data": data
        }
        return JsonResponse(response)

def years(request, format=None):
    if request.method == 'GET':
        years = []

        for product in OrderLineProduct.objects.all():
            if product.created_at.strftime("%d/%m/%Y")[6:10] not in years: 
                years.append(product.created_at.strftime("%d/%m/%Y")[6:10])

        response = {
            "status": "success",
            "data": years
        }

        return JsonResponse(response)
    else:
        return JsonResponse({
            "status": "fail"
        })

    JsonResponse({
        "status": "fail"
    })