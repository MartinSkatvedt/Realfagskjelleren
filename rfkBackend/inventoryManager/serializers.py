from rest_framework import serializers
from .models import Product, Merch, ProductCount, TotalProductCount

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image')


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('id', 'name', 'description', 'amount', 'price', 'image')

class ProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCount
        fields = ('id', 'date', 'amount', 'product')

class TotalProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalProductCount
        fields = ('id', 'date', 'author', 'data')
