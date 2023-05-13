from rest_framework import serializers
from User import models

#serializer class for serializing user data
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.UserModel
        fields = ['first_name','last_name','email','password','last_login','username','mobile','UserId','subscribedTo']
        