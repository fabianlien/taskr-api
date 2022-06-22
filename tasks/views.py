from taskr_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Task
from.serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks from all users
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.order_by('-due_by', '-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display a single task and provide RUD functionality if us is the owner
    """

    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.order_by('-created_at')
