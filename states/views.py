from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.request import Request

from .serializers import StepSerializer
from rest_framework import status



# Create your views here.

@api_view(["GET"])
def GetStepHandler(request: Request):
    return int(request.query_params.get('id', 'default'))
    

@api_view(["POST"])
def POSTStepHandler(request: Request):
    all_data=request.data
    serializer = StepSerializer(data=all_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
