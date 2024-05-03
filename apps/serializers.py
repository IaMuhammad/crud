from django.shortcuts import render
from rest_framework import serializers

from apps.models import Category, Product


# Create your views here.
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
