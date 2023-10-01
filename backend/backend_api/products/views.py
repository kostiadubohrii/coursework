from .models import Product, Reviews, ReviewLine
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def products_list(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def product_review_list(request, format=None):
    if request.method == 'POST':
        data = request.data
        product_id = data.get('product')
        user_id = data.get('user')
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            updateMeanReview(product_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT', 'POST', 'DELETE'])
def product_reviews_detail(request, id, format=None):

    try: 
        review = Reviews.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            updateMeanReview(request.data.get('product'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def updateMeanReview(product_id):
    reviews_tuple = Reviews.objects.filter(product=product_id)
    
    i = 0
    total_review = 0
    for review_tuple in reviews_tuple:
        total_review += review_tuple.review
        i+=1

    if i: 
        mean_review = round(total_review/i, 1)
    else:
        mean_review = 0
    
    if ReviewLine.objects.filter(product=product_id):
        product = ReviewLine.objects.get(product=product_id)
        product.meanReview = mean_review
        product.save()
    else: 
        product = ReviewLine(product=Product.objects.get(pk=product_id), meanReview=mean_review)
        product.save()

    product = Product.objects.get(pk=product_id)
    product.meanReview = ReviewLine.objects.get(product=product_id).meanReview
    product.save()