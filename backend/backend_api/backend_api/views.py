from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from orders.models import Order
from orderline.models import OrderLine, OrderLineProduct
from products.models import Product

def statistics(request):
    return render(request, 'statistics/statistics.html')

def statistics_data(request):
    orders_list = list(OrderLine.objects.values())
    orders_products_list = list(OrderLineProduct.objects.values())
    products = list(Product.objects.values())

    context = {
        "orders": orders_list,
        "orderedProduts": orders_products_list,
        "products": products
    }
      # Replace YourModel with your actual model
    return JsonResponse(context, safe=False)

def documentation(request):
    return render(request, 'documentation.html',  locals())