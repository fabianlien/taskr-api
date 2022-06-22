from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes all user profiles and displays all model fields.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'profile_image'
        ]
