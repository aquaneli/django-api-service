from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.request import Request
from .models import Event
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["POST"])
def PostCreateConversationHandler(request: Request):
    user_id = request.data.get('user_id')
    name = request.data.get('name')
    type = request.data.get('type')
    text = request.data.get('text')
    Event.objects.create(user_id=user_id, name=name, type=type, text=text)
    return JsonResponse("Created", safe=False)