from django.shortcuts import render
from rest_framework import viewsets

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


# Create your views here.
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
