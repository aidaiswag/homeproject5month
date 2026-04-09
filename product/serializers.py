from rest_framework import serializers
from .models import Product, Category, Review
from collections import Counter


from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']   


class ProductListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    review_list = serializers.SerializerMethodField()
    stars_avg = serializers.SerializerMethodField()

    
    def get_stars_avg(self, obj):
            return obj.reviews.all().aggregate(Avg('stars'))['stars__avg']

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'reviews', 'review_list', 'stars_avg']

    def get_review_list(self, obj):
        return [review.text for review in obj.reviews.all()]
    
             

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
            model = Product
            fields = '__all__'  

class CategoryListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'count'] 

    def get_count(self, obj):
        return obj.product.all().count()
    
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'product']                     


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'           