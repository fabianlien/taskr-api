from taskr_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Task, TaskItem
from.serializers import TaskSerializer, TaskItemSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks from all users and create functionality
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.order_by(
        'is_completed',
        'due_by',
        '-created_at',
        '-is_important',
    )
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = ['title']
    filterset_fields = [
        'owner__profile',
        'is_public',
        'is_completed',
        'requested_ID',
        'request_accepted'
    ]

    def perform_create(self, serializer):
        owner = self.request.user
        if serializer.validated_data.get("request_accepted") == "no":
            owner = User.objects.get(
                username=serializer.validated_data.get('owner').get('username')
            )
        serializer.save(owner=owner)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display a single task and provide CRUD functionality if user is the owner
    """

    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.order_by('-created_at')

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class TaskItemList(generics.ListCreateAPIView):
    """
    List all tasks or provides filter 
    for a specific task and create functionality
    """
    serializer_class = TaskItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskItem.objects.all().order_by('is_completed', 'created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task_id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskItem.objects.all()
