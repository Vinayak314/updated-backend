from rest_framework import serializers
from .models import Auction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'