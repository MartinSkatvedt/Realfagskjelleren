from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope 

from .serializers import ProductSerializer, MerchSerializer, ProductCountSerializer, TotalProductCountSerializer
from .models import Product, Merch, ProductCount, TotalProductCount

class ProductView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class MerchView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = MerchSerializer
    queryset = Merch.objects.all()

class ProductCountView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = ProductCountSerializer
    queryset = ProductCount.objects.all()

class TotalProductCountView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = TotalProductCountSerializer
    queryset = TotalProductCount.objects.all()
