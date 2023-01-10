from rest_framework import generics, filters
from django.db.models import Count
from taskr_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        tasks_count=Count('owner__task', distinct=True),
    ).order_by('tasks_count')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'name'
    ]
    ordering_fields = [
        'tasks_count',
        '-created_at',
        'updated_at'
        ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        tasks_count=Count('owner__task', distinct=True),
    ).order_by('tasks_count')
    serializer_class = ProfileSerializer
    ordering_fields = ['tasks_count']
