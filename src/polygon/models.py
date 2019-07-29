from django.conf import settings
from djgeojson.fields import PolygonField
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.db import models

class Polygons(models.Model):
    

    polygon_id      = models.AutoField(primary_key=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    Name            = models.CharField(max_length=120, null=False, blank= False )
    Price           = models.DecimalField(max_digits=10, decimal_places=2)
    Polygon         = PolygonField()
    
    def __str__(self):
        return str(self.user.email)
    @property
    def owner(self):
        return self.user