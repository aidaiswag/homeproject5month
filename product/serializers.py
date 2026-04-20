from rest_framework import serializers
from .models import Product, Category, Review
from collections import Counter
from rest_framework.exceptions import ValidationError


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



class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id    
    
class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=255)    

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length = 2, max_length=355)  
    stars = serializers.FloatField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist')
        return product_id    
