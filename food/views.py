from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from .serializers import foodSerializer

# Create your views here.


#-------------FOR ALL HOUSING-------------#
@api_view(['GET'])
def getFood(request):
    food = Food.objects.all()
    serializer = foodSerializer(food,many=True)
    return Response(serializer.data)