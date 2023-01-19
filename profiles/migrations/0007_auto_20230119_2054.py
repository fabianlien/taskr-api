# Generated by Django 3.2.13 on 2023-01-19 20:54

from django.db import migrations, models
import profiles.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='../default_profile_x3wzpb', upload_to='images/', validators=[profiles.validators.validate_file_size]),
        ),
    ]
