from taskr_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from.serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks from all users
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.order_by('-due_by', '-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = ['title']
    filterset_fields = [
        'owner__profile',
        'is_public'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display a single task and provide RUD functionality if us is the owner
    """

    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.order_by('-created_at')
