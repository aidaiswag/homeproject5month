from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product')

    def __str__(self):
        return self.title
    
    # def review_list(self):
    #     return [ку.text for i in self.]


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(null=True, choices=((i,i) for i in range(1,6)))

    def __str__(self):
        return self.text
    
    @property
    def review_list(self):
        return [i.text for i in self.product.all()]

