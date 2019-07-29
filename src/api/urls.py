from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet , userListView , userUpdateView ,userDeleteView,userCreateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('auth/', include('rest_auth.urls')),
    url('list/', userListView.as_view(),name='post-create-list'),
    url('update/(?P<pk>\d+)/$', userUpdateView.as_view(),name='post-update'),
    url('delete/(?P<pk>\d+)/$', userDeleteView.as_view(),name='post-delete'),
    url('create/', userCreateView.as_view(),name='post-create'),    
]