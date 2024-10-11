# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Category, Product
 
# Create a model serializer
class CategorySerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

