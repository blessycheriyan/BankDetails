from rest_framework import serializers
from.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankdetails
        fields = '__all__'