from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.pagination import PageNumberPagination
from .models import Product, Category, Review
from .serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    ReviewListSerializer,
    ReviewDetailSerializer,
    ProductValidateSerializer,
    CategoryValidateSerializer,
    ReviewValidateSerializer
    )
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer 
    pagination_class = CustomPagination


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'




