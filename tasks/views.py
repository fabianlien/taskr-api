from taskr_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskItem
from.serializers import TaskSerializer, TaskItemSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks from all users and create functionality
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.order_by(
        'is_completed',
        '-is_important',
        'due_by',
        '-created_at'
    )
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = ['title']
    filterset_fields = [
        'owner__profile',
        'is_public',
        'is_completed'
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


class TaskItemList(generics.ListCreateAPIView):
    """
    List all tasks for a specific task and create functionality
    """
    serializer_class = TaskItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TaskItem.objects.all().order_by('updated_at', 'created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskItem.objects.all()
