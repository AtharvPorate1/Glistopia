from django.shortcuts import render
from serializers import UserSerializer
from models import UserModel
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#creating a view for displaying user data , for creating user , updating user data , deleting user data
class UserList(APIView):
    #creating method for returning all user data
    def get(self, request, format=None):

        users = UserModel.objects.all()
        serializer = UserSerializer(users,many=)
        return Response(serializer.data)
    
#getting information about a particular user
class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist :
            raise Http404
    
    #getting user particular data
    def get(self , request , pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user , many=True)
        return Response(serializer.data)
    
    #checking fo username existance
    def UserExist(self , username):
        user = UserModel.objects.get(username=username)
        if user != None :
            return user
        return False
    #creating a user 
    def post(self,request , username):
        obj = self.UserExist(username)
        if obj != False :
            return Response({'error' : f'username {username} already exist use different username to create account','status' :status.HTTP_226_IM_USED})
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_created)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    


    #getting information about a particular user
    


