from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Mess.models import MessData
from Mess import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#class for calling all the data from the mess model and listing all mess information
class MessList(APIView):
            "list all mess data or create a new instance for mess"

            def get(self , request , format=None):
                    messData = MessData.objects.all()
                    serializer = serializers.MessDataSerializer(messData , many= True)
                    return Response(serializer.data)
            
            def post(self , request , format=None):
                    serializer = serializers.MessDataSerializer(data=request.data )
                    if serializer.is_valid() :
                            serializer.save()
                            return Response(serializer.data , status=status.HTTP_201_CREATED)
                    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
            
class MessDetail(APIView):
        def get_object(self, pk):
            try:
                return MessData.objects.get(pk=pk)
            except MessData.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            mess = self.get_object(pk)
            serializer = serializers.MessDataSerializer(mess)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            snippet = self.get_object(pk)
            serializer = serializers.MessDataSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
