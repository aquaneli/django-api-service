from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .models import Answer, Trigger, Condition
from rest_framework import status
from rest_framework.request import Request

@api_view(["GET"])
def GetAnswerHandler(request: Request):
    handler_id = int(request.query_params.get('id', '-1'))
    resp = {
        "error": True,
        "message": "Not found",
        "data": {},
    }
    if handler_id == '-1':
        answers = Answer.objects.all()
        resp["error"] = False
        resp["message"] = "OK"
        resp["data"] = []
        for a in answers:
            kb = {}
            if a.kb is not None:
                buttons = []
                for b in a.kb.buttons.all():
                        buttons.append({
                            "caption": b.caption,
                            "data": b.callback,
                            "row": b.row,
                            "order": b.order
                        })
                kb.update({
                    "type": a.kb.type,
                    "buttons": buttons
                })
            conditions = []
            if a.conditions is not None:
                for cond in a.conditions.all():
                    conditions.append({
                        "caption": cond.caption,
                        "variable
                        "operation": cond.operation,
                        "value": cond.value
                    })
            resp["data"].append({
                "trigger": {
                    "id": a.trigger.pk,
                    "type": a.trigger.type,
                    "content": a.trigger.cont
                },
                "id": a.pk,
                "answer": a.answer,
                "isKb": a.kb is not None,
                "keyboard": kb,
                "conditions": conditions,
                "set_variable": a.set_variable,
                "set_value": a.set_value,
                "state": a.state
            })
        return JsonResponse(resp, safe=False)

    try:
        content=Answer.objects.get(pk=handler_id)
        buttons = []
        kb = {}
        if content.kb is not None:
            for b in content.kb.buttons.all():
                buttons.append({
                    "caption": b.caption,
                    "data": b.callback,
                    "row": b.row,
                    "order": b.order
                })
            kb.update({
                "type": content.kb.type,
                "buttons": buttons
            })
        conditions = []
        if content.conditions is not None:
            for cond in content.conditions.all():
                conditions.append({
                    "caption": cond.caption,
                    "variable": cond.variable,
                    "operation": cond.operation,
                    "value": cond.value
                })
        resp.update({
            "error": False,
            "message": "Success",
            "data": {
                "id": content.pk,
                "answer":content.answer,
                "isKb": content.kb is not None,
                "keyboard": kb,
                "conditions": conditions,
                "set_variable": content.set_variable,
                "set_value": content.set_value,
                "state": content.state,
                "nextState": content.next_state,
                "delay": content.delay,
                "isNextMsg": content.next_msg is not None,
                "nextMsg": content.next_msg.pk if content.next_msg is not None else None
            }
        })
    except: pass
    return JsonResponse(resp, status=status.HTTP_200_OK, safe=False)

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
                    buttons.append({
                        "caption": b.caption,
                        "data": b.callback,
                        "row": b.row,
                        "order": b.order
                    })
                kb.update({
                    "type": c.kb.type,
                    "buttons": buttons
                })
            conditions = []
            if c.conditions is not None:
                for cond in c.conditions.all():
                    conditions.append({
                        "caption": cond.caption,
                        "variable": cond.variable,
                        "operation": cond.operation,
                        "value": cond.value
                    })
            resp.append(
                {
                    "id": c.pk,
                    "answer":c.answer,
                    "isKb": iskb,
                    "keyboard": kb,
                    "conditions": conditions,
                    "set_variable": c.set_variable,
                    "set_value": c.set_value,
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
                    buttons.append({
                        "caption": b.caption,
                        "data": b.callback,
                        "row": b.row,
                        "order": b.order
                    })
                kb.update({
                    "type": c.kb.type,
                    "buttons": buttons
                })
            conditions = []
            if c.conditions is not None:
                for cond in c.conditions.all():
                    conditions.append({
                        "caption": cond.caption,
                        "variable": cond.variable,
                        "operation": cond.operation,
                        "value": cond.value
                    })
            resp.append(
                {
                    "id": c.pk,
                    "answer":c.answer,
                    "isKb": iskb,
                    "keyboard": kb,
                    "conditions": conditions,
                    "set_variable": c.set_variable,
                    "set_value": c.set_value,
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
def GetCallbackAnswerHandler(request: Request):
    callbackreq=request.query_params.get('callback', 'default')
    trigger=Trigger.objects.get(cont=callbackreq, type="clbck")
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
                    buttons.append({
                        "caption": b.caption,
                        "data": b.callback,
                        "row": b.row,
                        "order": b.order
                    })
                kb.update({
                    "type": c.kb.type,
                    "buttons": buttons
                })
            conditions = []
            if c.conditions is not None:
                for cond in c.conditions.all():
                    conditions.append({
                        "caption": cond.caption,
                        "variable": cond.variable,
                        "operation": cond.operation,
                        "value": cond.value
                    })
            resp.append(
                {
                    "id": c.pk,
                    "answer":c.answer,
                    "isKb": iskb,
                    "keyboard": kb,
                    "conditions": conditions,
                    "set_variable": c.set_variable,
                    "set_value": c.set_value,
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