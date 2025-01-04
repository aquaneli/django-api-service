from rest_framework import serializers
from .models import StateManagment

class StateManagmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateManagment
        fields = ['profile_id', 'state']