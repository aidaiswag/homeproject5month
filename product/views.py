from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category, Review
from .serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    ReviewListSerializer,
    ReviewDetailSerializer
    )


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.prefetch_related('category', 'reviews').all()
        data = ProductListSerializer(product, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

    product = Product.objects.create(
        title=title,
        description=description,
        price=price,
        category_id=category_id
    )
    return Response(status=status.HTTP_201_CREATED,
                    data=ProductDetailSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_200_OK, 
                        data=ProductDetailSerializer(product).data)





@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        data = CategoryListSerializer(category, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')

    category = Category.objects.create(
        name = name
    )
    return Response (status=status.HTTP_201_CREATED,
                     data=CategoryDetailSerializer(category).data)

@api_view(['GET', 'DELETE', 'PUT'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategoryDetailSerializer(category, many=False).data
        return Response(data=data)
    if request.method == 'DELETE':
        category.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response (status=status.HTTP_200_OK,
                         data=CategoryDetailSerializer(category).data)



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewListSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
    review = Review.objects.create(
        text = text,
        stars =stars,
        product_id=product_id
    )    
    return Response(status=status.HTTP_201_CREATED,
                    data=ReviewDetailSerializer(review).data)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(review, many=False).data
        return Response(data=data)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response(status=status.HTTP_200_OK,
                        data=ReviewDetailSerializer(review).data)
        

@api_view(['GET'])
def product_reviews_view(request):
    products = Product.objects.prefetch_related('reviews')
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)