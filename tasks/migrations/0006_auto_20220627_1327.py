# Generated by Django 3.2.13 on 2022-06-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_taskitem_attached_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='attached_file',
            field=models.FileField(blank=True, upload_to='task_items/'),
        ),
        migrations.AddField(
            model_name='taskitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
