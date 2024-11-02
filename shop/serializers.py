from rest_framework import serializers
from shop.models import Category, Product, Article




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 
                 'description', 'active', 'category']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']

    def validate_name(self, value):
        if self.instance is None:  # Only check on create
            if Category.objects.filter(name=value).exists():
                raise serializers.ValidationError({
                    'name': [
                        {
                            'message': 'Category already exists',
                            'code': 'unique'
                        }
                    ]
                })
        return value

    def validate(self, data):
        if 'description' in data and 'name' in data:
            if data['description'] and data['name'] not in data['description']:
                raise serializers.ValidationError({
                    'description': [
                        {
                            'message': 'Name must be in description',
                            'code': 'invalid'
                        }
                    ]
                })
        return data

    def create(self, validated_data):
        # Ensure description exists
        if 'description' not in validated_data:
            validated_data['description'] = ''
        return super().create(validated_data)


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 
                 'description', 'active', 'products']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 
                 'description', 'active', 'price', 'product']