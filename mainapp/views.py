from rest_framework.viewsets import ModelViewSet

from mainapp.models import Todo,User

from mainapp.serializer import TodoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

class TodoView(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
    def list(self, request, *args, **kwargs):
        todoes=Todo.objects.filter(user=request.user)
        return Response(TodoSerializer(instance=todoes,many=True).data)
    