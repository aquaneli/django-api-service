from django.shortcuts import render

from rest_framework.decorators import api_view

from django.http.response import JsonResponse

from rest_framework import status

from .serializers import KeyboardSerializer
from .models import Keyboard


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
        content=Keyboard.objects.get(triggers=handler_triggers)
        serializer = KeyboardSerializer(content)
        print(content)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    except: pass

    return JsonResponse(handler_triggers, safe=False)

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