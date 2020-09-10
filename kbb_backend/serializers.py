from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoefields = '__all__'