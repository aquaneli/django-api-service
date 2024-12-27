from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.request import Request

# Create your views here.

# @api_view(["GET"])
# def GetAnswerHandler(request: Request):
#     int(request.query_params.get('id', 'default'))