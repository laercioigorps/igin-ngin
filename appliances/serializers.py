from rest_framework import serializers
from .models import Appliance, Brand, Category


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ApplianceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appliance
        fields = ['model', 'category', 'brand']
