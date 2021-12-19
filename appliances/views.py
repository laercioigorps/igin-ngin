from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from appliances import serializers
from appliances.models import Brand, Category
from appliances.serializers import BrandSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.


@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def brand_list_view(request, format=None):
    if(request.method == 'GET'):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=400)


@api_view(['GET'])
def brand_detail_view(request, pk, format=None):
    if(request.method == 'GET'):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def category_list_view(request, format=None):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    if(request.method == 'GET'):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
