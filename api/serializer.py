from rest_framework import serializers 
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class FilterItemSerialer(serializers.Serializer):
    status = serializers.BooleanField(required=False)
    name = serializers.CharField(required=False)
    max_amot = serializers.FloatField(required=False)
    min_amout = serializers.FloatField(required=False)
