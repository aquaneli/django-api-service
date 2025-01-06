from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.request import Request

from rest_framework import status
from .models import StateManagment



# Create your views here.

@api_view(["GET"])
def GetStateHandler(request: Request):
    handler_id = int(request.query_params.get('id'))
    try:
        state = StateManagment.objects.get(profile_id=handler_id)
        resp = {
            "profile_id": state.profile_id,
            "state": state.state
        }
        return JsonResponse(resp, safe=False)
    except:
        return JsonResponse("None", safe=False)
    
    

@api_view(["POST"])
def POSTStateHandler(request: Request):
    data = request.data
    try:
        state = StateManagment.objects.get(profile_id=int(data["profile_id"]))
        state.state = data["state"]
        state.save()
        dataresp = {
            "profile_id": state.profile_id,
            "state": state.state
        }
        return JsonResponse(dataresp, status=status.HTTP_200_OK, safe=False)
    except:
        state = StateManagment.objects.create(profile_id=int(data["profile_id"]), state=data["state"])
        dataresp = {
            "profile_id": state.profile_id,
            "state": state.state
        }
        return JsonResponse(dataresp, status=status.HTTP_201_CREATED, safe=False)