from rest_framework import serializers
from django.core.serializers import serialize
from polygon.models import Polygons


class PolygonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygons
        fields = [
            'polygon_id',
            'user',
            'Name',
            'Price',
            'Polygon'
            
        ]
        
        read_only_fields = ['user','polygon_id']
