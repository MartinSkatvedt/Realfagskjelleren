from rest_framework import serializers
from .models import Product, Merch

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image')


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('id', 'name', 'description', 'amount', 'price', 'image')