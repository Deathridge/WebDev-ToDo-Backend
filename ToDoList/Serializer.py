from rest_framework import serializers
from django.contrib.auth.models import User
from ToDoList.models import Task, Item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        lookup_field = 'username'
        model = User 
        exclude = ('user_permissions',)
        
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']            
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
    
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item