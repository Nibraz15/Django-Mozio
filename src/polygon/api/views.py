import json
from django.http import HttpResponse
from rest_framework import generics
from polygon.models import Polygons
from .serializers import PolygonsSerializer 
from .permissions import IsOwnerOrReadOnly 
from django.contrib.gis.geos import Point, Polygon
class PolyonssRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'pk'
    serializer_class = PolygonsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    

    def get_queryset(self):
        return Polygons.objects.all()

class PolyonssListCreateView(generics.ListCreateAPIView):
    
    
    serializer_class = PolygonsSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Polygons.objects.filter(user=user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    
    
  
    