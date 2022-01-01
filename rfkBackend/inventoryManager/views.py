from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, MerchSerializer
from .models import Product, Merch


class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class MerchView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MerchSerializer
    queryset = Merch.objects.all()