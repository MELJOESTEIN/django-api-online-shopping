from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shop.models import Category, Product, Article


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product  
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 
                 'active', 'category']  # Added relevant product fields


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']


class CategoryDetailSerializer(ModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 
                 'active', 'products']  # Specified all fields explicitly

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data


class ArticleSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)  # Added product relationship
    
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 
                 'price', 'product', 'active']  # Added id, product and active fields