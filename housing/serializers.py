from rest_framework.serializers import ModelSerializer
from .models import housing

class housingSerializer(ModelSerializer):
    class Meta:
        model = housing
        fields = '__all__'