from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import housing
from .serializers import housingSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {"time":{"updated":"Mar 17, 2023 17:54:00 UTC","updatedISO":"2023-03-17T17:54:00+00:00","updateduk":"Mar 17, 2023 at 17:54 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"26,498.3958","description":"United States Dollar","rate_float":26498.3958},"GBP":{"code":"GBP","symbol":"&pound;","rate":"22,141.8475","description":"British Pound Sterling","rate_float":22141.8475},"EUR":{"code":"EUR","symbol":"&euro;","rate":"25,813.3062","description":"Euro","rate_float":25813.3062}}}
    ]
    return Response(routes)


#-------------FOR ALL HOUSING-------------#
@api_view(['GET'])
def getHousing(request):
    house = housing.objects.all()
    serializer = housingSerializer(house,many=True)
    return Response(serializer.data)


#TO GET A SPECIFIC HOUSE
@api_view(['GET'])
def getHouse(request,pk):
    house = housing.objects.get(id=pk)
    serializer = housingSerializer(house,many=False)
    return Response(serializer.data)