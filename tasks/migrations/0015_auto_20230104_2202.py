# Generated by Django 3.2.13 on 2023-01-04 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0014_alter_task_requested_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='requested_by',
        ),
        migrations.AddField(
            model_name='task',
            name='requested_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_ID', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='requested_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]