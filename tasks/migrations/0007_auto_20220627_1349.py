# Generated by Django 3.2.13 on 2022-06-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20220627_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskitem',
            name='attached_file',
        ),
        migrations.RemoveField(
            model_name='taskitem',
            name='is_completed',
        ),
    ]