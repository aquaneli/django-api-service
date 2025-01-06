from rest_framework import serializers
from .models import Profile, UserProfile
from content.serializers import StatusSerializer



class ProfileSerializer(serializers.ModelSerializer):
    statuses = StatusSerializer(read_only=True)
    class Meta:
        fields="__all__"
        model=Profile
        
class UserProfileSerializer(serializers.ModelSerializer):
    statuses = StatusSerializer(read_only=True, many=True)
    class Meta:
        fields="__all__"
        model=UserProfile
