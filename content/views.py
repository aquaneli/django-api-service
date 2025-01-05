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
def GetTextAnswerHandler(request: Request):
    handler_triggers = request.query_params.get('text', 'default')
    resp=[]
    try:
        trigger=Trigger.objects.get(cont=handler_triggers, type="text")
        content=Answer.objects.filter(trigger=trigger).all()
        for c in content:
            buttons = []
            kb = {}
            iskb = False
            if c.kb is not None:
                iskb = True
                for b in c.kb.buttons.all():
                    buttons.append(b.caption)
                kb.update({
                    "type": c.kb.type,
                    "buttons": buttons
                })
            resp.append(
                {
                    "id": c.pk,
                    "answer":c.answer,
                    "isKb": iskb,
                    "keyboard": kb,
                    "state": c.state,
                    "nextState": c.next_state,
                    "delay": c.delay,
                    "isNextMsg": c.next_msg is not None,
                    "nextMsg": c.next_msg.pk if c.next_msg is not None else None
                }
            )

        return JsonResponse(resp, safe=False)
    except: pass

    return JsonResponse(resp, safe=False)

@api_view(["GET"])
def GetCMDAnswerHandler(request: Request):
    cmdreq=request.query_params.get('cmd', 'default')
    trigger=Trigger.objects.get(cont=cmdreq, type="cmd")
    resp=[]
    try:
        content=Answer.objects.filter(trigger=trigger).all()
        for c in content:
            buttons = []
            kb = {}
            iskb = False
            if c.kb is not None:
                iskb = True
                for b in c.kb.buttons.all():
                    buttons.append(b.caption)
                kb.update({
                    "type": c.kb.type,
                    "buttons": buttons
                })
            resp.append(
                {
                    "id": c.pk,
                    "answer":c.answer,
                    "isKb": iskb,
                    "keyboard": kb,
                    "state": c.state,
                    "nextState": c.next_state,
                    "delay": c.delay,
                    "isNextMsg": c.next_msg is not None,
                    "nextMsg": c.next_msg.pk if c.next_msg is not None else None
                }
            )

        return JsonResponse(resp, safe=False)
    except: pass
    return JsonResponse(resp, safe=False)