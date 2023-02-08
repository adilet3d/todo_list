from rest_framework import serializers

from mainapp.models import Todo, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields=(
            'id','user','name',
            'description','image',
            'created_at','deadline',
            'is_done',
        )
        read_only_fields=(
            'user','created_at',
        )

class UserSerializer(serializers.ModelSerializer):
    todoes= TodoSerializer(read_only=True, many =True)
    class Meta:
        model=User
        fields= ('id','username','todoes')