from rest_framework import serializers
from .models import BotConfig

class BotConfigSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=BotConfig
    