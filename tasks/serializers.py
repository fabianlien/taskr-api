from rest_framework import serializers
from .models import Task, TaskItem


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
            'id', 'owner', 'title', 'is_owner', 'is_public',
            'created_at', 'updated_at', 'due_by', 'description',
            'is_completed', 'is_important'
        ]


class TaskItemSerializer(serializers.ModelSerializer):
    """
    Serializes all user tasks and displays all model fields.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TaskItem
        fields = [
            'id', 'owner', 'task_id', 'content', 'created_at', 'updated_at',
            'is_owner', 'is_completed', 
            # 'attached_file'
        ]
