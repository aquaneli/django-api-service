from django.shortcuts import render

from rest_framework.decorators import api_view
import rest_framework

from django.http.response import JsonResponse
import rest_framework.request

from rest_framework import status

from .serializers import MessageSerializer
from .models import Message

from .serializers import ProfileSerializer
from .models import Profile

from .serializers import AnswerSerializer
from .models import Answer, Trigger



from rest_framework.request import Request


@api_view(["GET"])
def GetContentHandler(request: Request):
    handler_triggers = request.query_params.get('triggers', 'default')
    # handler_buttons = request.query_params.get('buttons', 'default')
    # handler_keyboards = request.query_params.get('keyboards', 'default')
    # handler_messages = request.query_params.get('messages', 'default')
    # result = []
    print(handler_triggers)
    
    try:
        # content = Message.objects.get(triggers=handler_triggers, buttons=handler_buttons,keyboards= handler_keyboards,messages=handler_messages)
        # result.append(content.triggers, content.buttons, content.keyboards, content.messages)
        content=Message.objects.get(triggers=handler_triggers)
        serializer = MessageSerializer(content)
        print(content)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    except: pass

    return JsonResponse(handler_triggers, safe=False)

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


@api_view(["GET"])
def GetAnswerHandler(request: Request):
    cmdreq=request.query_params.get('cmd', 'default')
    trigger=Trigger.objects.get(cont=cmdreq)
    resp=[]
    try:
        content=Answer.objects.filter(trigger=trigger).all()
        for c in content:
            resp.append(
                {
                    "answer":c.answer,
                    "trigger":{
                        "cont": c.cont,
                        "type": c.type
                    }
                }
            )

        
        
        
        
        return JsonResponse(resp, safe=False)
    except: pass
    return JsonResponse(resp, safe=False)