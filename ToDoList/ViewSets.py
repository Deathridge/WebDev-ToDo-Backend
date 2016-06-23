from rest_framework import viewsets
from ToDoList.Serializer import UserSerializer,TaskSerializer
from ToDoList.models import Task
from django.contrib.auth.models import User,Permission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@permission_classes((AllowAny, ))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
    	if self.request.user.is_superuser:
        	return User.objects.all()
    	else:
        	return User.objects.filter(id=self.request.user.id)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
    def get_queryset(self):
        username = self.request.user
        if username.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(creator=username)
    
    def perform_create(self, serializer):   
        serializer.save(creator = self.request.user)
