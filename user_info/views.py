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
    resp = {
        "error": True,
        "message": "Not found"
    }
    try:
        content= Profile.objects.get(id=handler_id)
        sts = []
        statuses = content.statuses.all()
        for s in statuses:
            print(s)
            sts.append(s.caption)
        print(sts)
        
        result = {
            "id": content.id,
            "active": content.active,
            "registered": content.registered,
            "statuses": sts,
            "last_visit": content.last_visit,
            "is_admin": content.is_admin,
            "achives": content.achives
        }
        resp.update({
            "error": False,
            "message": "Ok",
            "data": result
        })

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
    data = {
        "id": p.tgid,
        "active": p.active,
        "registered": p.registered,
        "statuses": [s.caption for s in p.statuses.all()],
        "last_visit": p.last_visit,
        "is_admin": p.is_admin,
        "achives": p.achives
    }
    
    return JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)
