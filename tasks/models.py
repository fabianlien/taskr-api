from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # cluster = models.ForeignKey(Cluster, on_delete=models.CASCASDE)
    # requested_by = models.???
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_by = models.DateTimeField(blank=True)
    description = models.TextField(max_length=300, blank=True)
    is_overdue = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-due_by', '-created_at']

    def __str__(self):
        return f'{self.title}'
