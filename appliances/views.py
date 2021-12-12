from django.shortcuts import render
from appliances.serializers import BrandSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.


@api_view(['POST'])
def brand_list_view(request, format=None):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=400)
