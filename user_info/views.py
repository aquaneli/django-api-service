import datetime
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from .models import Profile
from .models import Status
from .models import Achive

@api_view(["PATCH"])
def ProfileUpdateHandler(request: Request):
    data = request.data
    try:
        p = Profile.objects.get(tgid=int(data["id"]))
        p.last_visit = datetime.datetime.now()
        p.save()
        return JsonResponse(status=status.HTTP_200_OK, data={"message": "Success"}, safe=False)
    except: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={"message": "Profile not found"}, safe=False)

@api_view(["GET", "POST"])
def ProfileHandler(request: Request):
    match request.method:
        case "GET":
            handler_id = int(request.query_params.get('id', '-1'))
            resp = {
                "error": True,
                "message": "Not found",
                "data": {},
            }
            if handler_id == -1:
                profiles = Profile.objects.all()
                result = []
                for p in profiles:
                    sts = []
                    statuses = p.statuses.all()
                    for s in statuses:
                        sts.append(s.caption)
                    result.append({
                        "id": p.tgid,
                        "active": p.active,
                        "registered": p.registered,
                        "statuses": sts,
                        "last_visit": p.last_visit,
                        "is_admin": p.is_admin,
                        "achives": [a.caption for a in p.achives.all()]
                    })
                resp.update({
                    "error": False,
                    "message": "Ok",
                    "data": result
                })
                return JsonResponse(resp, status=status.HTTP_200_OK, safe=False)
            try:
                content= Profile.objects.get(tgid=handler_id)
                sts = []
                achives = []
                for a in content.achives.all():
                    achives.append(a.caption)
                statuses = content.statuses.all()
                for s in statuses:
                    sts.append(s.caption)
                
                result = {
                    "id": content.tgid,
                    "active": content.active,
                    "registered": content.registered,
                    "statuses": sts,
                    "last_visit": content.last_visit,
                    "is_admin": content.is_admin,
                    "achives": achives
                }
                resp.update({
                    "error": False,
                    "message": "Ok",
                    "data": result
                })

                return JsonResponse(resp, status=status.HTTP_200_OK, safe=False)
            except: pass

            return JsonResponse(resp, status=status.HTTP_404_NOT_FOUND, safe=False)
        
        case "POST":
            
            all_data=request.data
            try:
                p = Profile.objects.get(tgid=int(all_data.get("id")))
                return JsonResponse(status=status.HTTP_409_CONFLICT, data={"message": "Profile with this id already exists"}, safe=False)
            except: pass
            p=Profile.objects.create(
                tgid=int(all_data.get("id")),
                active=True,
                is_admin=all_data.get('is_admin', False),
            )
            
            for a in all_data["achives"]:
                try:
                    a = Achive.objects.get(caption = a)
                    p.achives.add(a)
                    continue
                except: 
                    a = Achive.objects.create(caption = a)
                    p.achives.add(a)
    
            for st in all_data["statuses"]:
                try:
                    s = Status.objects.get(caption = st)
                    p.statuses.add(s)
                    continue
                except: 
                    s = Status.objects.create(caption = st)
                    p.statuses.add(s)
                
            p.save()
            data = {
                "id": p.tgid,
                "active": p.active,
                "registered": p.registered,
                "statuses": [s.caption for s in p.statuses.all()],
                "last_visit": p.last_visit,
                "is_admin": p.is_admin,
                "achives": [a.caption for a in p.achives.all()]
            }
            
            return JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)
