from django.shortcuts import render
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
# Create your views here.


class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()