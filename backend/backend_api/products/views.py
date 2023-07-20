from .models import Product, Reviews
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def products_list(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_detail(request, id, format=None):

    try: 
        product = Product.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_review(request, format=None):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            reviews = Reviews.objects.all()
            mean_review = calculateMeanReview(reviews)
            # Update the review field in the Product instance
            product = serializer.instance.product
            product.review = review 
            product.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def calculateMeanReview(data_list):
    revs = 0
    i = 0
    for rev in data_list:
        revs += rev.user_review
        i += 1
    
    mean_review = round(revs/i, 1)
    return mean_review

reviews = Reviews.objects.all()
calculateMeanReview(reviews)

