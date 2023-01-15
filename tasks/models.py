from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_ID = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True,
        related_name='requested_ID'
    )
    requested_username = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_by = models.DateTimeField(blank=True)
    description = models.TextField(max_length=300, blank=True)
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    request_accepted = models.CharField(
        blank=True, default='0', max_length=5
        )

    class Meta:
        ordering = ['due_by']

    def __str__(self):
        return f'{self.title}'


class TaskItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_id'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=150)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['updated_at', 'created_at']

    def __str__(self):
        return f'{self.content}'
