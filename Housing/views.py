from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Housing.models import HousingModels
from Housing import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class HousingList(APIView):

    def get(self , request):
        houses = HousingModels.objects.all()
        houseSerializer = serializers.HousingSerializer(houses , many = True)
        return Response(houseSerializer.data)
    
    def get(self , request , pk):
        houses = HousingModels.objects.get(pk = pk)
        if houses.DoesNotExist :
            raise Http404 
        houseSerializer = serializers.HousingSerializer(houses )
        return Response(houseSerializer.data)

    