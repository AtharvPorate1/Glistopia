from rest_framework import serializers
from Mess import models

class MessDataSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.MessData
        fields = ['messName' ,'contactNo' ,'profile' ,'email','location']
        