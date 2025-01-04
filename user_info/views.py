from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from .models import Profile
from .models import Status

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



@api_view(["POST"])
def POSTProfileHandler(request: Request):
    all_data=request.data
    p=Profile.objects.create(
        tgid=int(all_data.get("id")),
        active=True,
        is_admin=all_data.get('is_admin', False),
        achives=all_data.get('achives', "")
    )
    
    for st in all_data["statuses"]:
        s = Status.objects.create(caption = st["caption"])
        s.save()
        p.statuses.add(s)
        
    p.save()
    
    return JsonResponse(status=status.HTTP_200_OK, data={"status":"Ok"}, safe=False)
    # resp=[]
    # resp.append(
    #     "id": all_data.id,
    #     "active": true,
    #     "registered": 10,
    #     "statuses":{
    #         "caption":10
    #     },
    #     "last_visit": 10,
    #     "is_admin": true,
    #     "achives": "field"
    # ) 
    # print(all_data)
    # serializer = ProfileSerializer(data=all_data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
