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
    products_ordered = list(OrderLineProduct.objects.all())
    order_lines = []
    for i in products_ordered: 
        orderline = {
            "orderline": i.orderline.orderLineId,
            "productId": i.product.pk,
            "quantity": i.quantity
        }
        order_lines.append(orderline)

    order_data = list(OrderLine.objects.all())
    order_datas = []

    for j in order_data: 
        order_data = {
            "created_at": j.created_at.strftime("%d/%m/%Y"),
            "id": j.orderLineId
        }
        order_datas.append(order_data)

    for item in order_datas:
        orderline_id = item.get('id')
        created_at = item.get('created_at')

        for entry in order_lines:
            entry_id = entry.get('orderline')

            if entry_id == orderline_id:
                entry['created_at'] = created_at


    def get_short_month(crated_at):
        date = datetime.strptime(crated_at, "%d/%m/%Y")
        month = calendar.month_name[date.month].lower()[0:3]
        return month

    def get_products_info_year(order_lines):
        prices = {}
        products_dict = Product.objects.all()
        
        for i in products_dict:
            produt_id = i.pk
            price = i.price
            prices[produt_id] = [price]

        results = {}
        for item in order_lines: 
            product_id = item.get('productId')
            product_name = Product.objects.get(pk=product_id).name
            crated_at = item.get('created_at')
            
            if not product_id in results:
                results[product_id] = {
                    "id": product_id,
                    "name": product_name,
                    "revenue": {"jan": 0,"feb": 0,"mar": 0,"apr": 0,"may": 0,"jun": 0,"jul": 0,"aug": 0,"sep": 0,"oct": 0,"nov": 0,"dec": 0},
                    "sells": {"jan": 0,"feb": 0,"mar": 0,"apr": 0,"may": 0,"jun": 0,"jul": 0,"aug": 0, "sep": 0,"oct": 0,"nov": 0,"dec": 0}
                }
                
                results[product_id]["revenue"][get_short_month(crated_at)] = item['quantity'] * prices[product_id][0]
                results[product_id]["sells"][get_short_month(crated_at)] = item['quantity']
                
            else: 
                results[product_id]["revenue"][get_short_month(crated_at)] += item['quantity'] * prices[product_id][0]
                results[product_id]["sells"][get_short_month(crated_at)] += item['quantity']

        return list(results.values())

    newData = {}

    for item in order_lines:
        year = datetime.strptime(item['created_at'], '%d/%m/%Y').year
        if year in newData: 
            newData[year].append(item)
        else:
            newData[year] = [item]
    
    for key in newData:
        year = newData[key]
        newData[key] = get_products_info_year(year)

    
    print(newData)
    
    return JsonResponse(newData)
        
    
