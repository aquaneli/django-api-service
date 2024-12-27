from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Profile
from django.http.response import JsonResponse

# Create your views here.

@api_view(["GET"])
def GetProfileHandler(request: Request):
    handler_id = int(request.query_params.get('id', 'default'))
    # handler_active = request.query_params.get('active', 'default')
    # handler_registered = request.query_params.get('registered', 'default')
    # handler_statuses = request.query_params.get('statuses', 'default')
    # handler_last_visit = request.query_params.get('last_visit', 'default')
    # handler_is_admin = request.query_params.get('is_admin', 'default')
    # handler_achives = request.query_params.get('achives', 'default')
    # handler_name = request.query_params.get('name', 'default')
    # print(handler_id)
    try:
        # content = Profile.objects.get(id=handler_id, active=handler_active, 
        #                               registered=handler_registered,statuses=handler_statuses, 
        #                               last_visit=handler_last_visit,is_admin=handler_is_admin,
        #                               achives=handler_achives,name=handler_name)
        content= Profile.objects.get(id=handler_id)
        sts = []
        statuses = content.statuses.all()
        for s in statuses:
            print(s)
            sts.append(s.caption)
        print(sts)
        
        resp = {
            "id": content.id,
            "active": content.active,
            "registered": content.registered,
            "statuses": sts,
            "last_visit": content.last_visit,
            "is_admin": content.is_admin,
            "achives": content.achives
        }

        return JsonResponse(resp, status=status.HTTP_200_OK, safe=False)
    except: pass

    return JsonResponse(handler_id, safe=False)