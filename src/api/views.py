from rest_framework import viewsets
from rest_framework import generics
from api.models import User
from api.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrReadOnly 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class userListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    
    
    def perform_create_list(self,serializer):
        serializer.save(user=self.request.user)

class userUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field            = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
   
    
    def perform_update(self,serializer):
        
        serializer.save(user=self.request.user)

class userDeleteView(generics.RetrieveDestroyAPIView):
    lookup_field            = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
   
    
    def perform_delete(self,serializer):
        
        serializer.save(user=self.request.user)

class userCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
    
    