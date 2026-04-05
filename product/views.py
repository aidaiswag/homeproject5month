from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Review
from rest_framework import status
from .serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    ReviewListSerializer,
    ReviewDetailSerializer
    )


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    data = ProductListSerializer(product, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    data = CategoryListSerializer(category, many=True).data
    return Response(data=data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)