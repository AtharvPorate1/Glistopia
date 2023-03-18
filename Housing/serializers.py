from rest_framework import serializers
from models import HousingModels

class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        models = HousingModels
        fields = ['location', 'Amenities','Rent','Deposit','AccomodationType']
        
