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

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    taskItems = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = Task
    
    def create(self, validated_data):
        items_data = validated_data.pop('taskItems')

        task = Task.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(taskItem=task, **item_data)
        return task