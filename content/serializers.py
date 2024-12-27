from rest_framework import serializers
from .models import Message, Profile, Status, Answer, Trigger

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Message

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Status
 
class ProfileSerializer(serializers.ModelSerializer):
    statuses = StatusSerializer(read_only=True)
    class Meta:
        fields="__all__"
        model=Profile

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Answer

class AnswerSerializer(serializers.ModelSerializer):
    trigger=TriggerSerializer(read_only=True)
    class Meta:
        fields="__all__"
        model=Answer
