from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.request import Request
from .models import Event

# Create your views here.

def GetConversationsHandler(request: Request):
    user_id = request.query_params.get('user_id')
    events = Event.objects.filter(user_id=user_id).all()
    return JsonResponse(events, safe=False)