from .views import PolyonssRudView , PolyonssListCreateView 
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$',PolyonssRudView.as_view(),name='post-create'),
    url('list/',PolyonssListCreateView.as_view(),name='post-rud'),
    
]