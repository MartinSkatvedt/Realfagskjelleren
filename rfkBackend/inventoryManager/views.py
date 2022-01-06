from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from oidc_provider.lib.utils.oauth2 import protected_resource_view

from .serializers import ProductSerializer, MerchSerializer, ProductCountSerializer, TotalProductCountSerializer
from .models import Product, Merch, ProductCount, TotalProductCount

class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class MerchView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MerchSerializer
    queryset = Merch.objects.all()

class ProductCountView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCountSerializer
    queryset = ProductCount.objects.all()

class TotalProductCountView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TotalProductCountSerializer
    queryset = TotalProductCount.objects.all()
