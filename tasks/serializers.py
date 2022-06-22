from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializes all user tasks and displays all model fields.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'title', 'is_owner', 'created_at',
            'updated_at', 'due_by', 'description', 'is_overdue',
            'is_completed', 'is_important'
        ]
