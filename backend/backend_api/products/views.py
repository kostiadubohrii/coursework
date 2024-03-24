from .models import Product, Reviews, ReviewLine, Category
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def products_list(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    # if request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             "status": "success",
    #             "data": serializer.data
    #         }, status=status.HTTP_201_CREATED)
        return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_detail(request, id, format=None):
    try: 
        product = Product.objects.get(pk=id)
    except:
        return Response({
                "status": "failure",
                "message": f"Product with id: {id} does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

def validateReview(review):
    if float(review) <= 5 and float(review) >= 0:
        return True
    else:
        return False
        

@api_view(['POST', 'GET'])
def product_review_list(request, format=None):
    if request.method == 'POST':
        data = request.data
        product_id = data.get('product')
        user_id = data.get('user')
        review = data.get('review')
        if Reviews.objects.filter(user=user_id, product=product_id).exists(): 
            return Response({
                "status": "failure",
                "message": f"User with user id: {user_id} has alredy left review.",
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            if validateReview(review):
                serializer = ReviewSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    updateMeanReview(product_id)
                    return Response({
                        "status": "success",
                        "data": serializer.data
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                            "status": "failure",
                            "message": "Review field must be in range 0 to 5",
                        }, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    serializer = ReviewSerializer(data=data)
    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH', 'DELETE'])
def product_reviews_detail(request, id, format=None):

    try: 
        review = Reviews.objects.get(pk=id)
    except:
        return Response({
                "status": "failure",
                "message": f"Review with id: {id} does not exist",
            },status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        if 'review' in request.data:
            if validateReview(request.data['review']):
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    product_id = Reviews.objects.get(pk=id).product.id
                    updateMeanReview(product_id)
                    return Response({
                        "status": "success",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK)
                return Response({
                        "status": "failure",
                        "data": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": "failure",
                    "message": "Review field must be in range 0 to 5",
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "status": "failure",
                "message": "A review's data can not be changed "
            }, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'DELETE':
        review.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def categories_list(request, format=None):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_details(request, id, format=None):
    try: 
        category = Category.objects.get(pk=id)
    except:
        return Response({
                "status": "failure",
                "message": f"Category with id: {id} does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    return Response({
                "status": "failure",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

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
