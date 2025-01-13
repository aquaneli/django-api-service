from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.request import Request

from rest_framework import status
from .models import StateManagment, Variable

@api_view(["GET", "POST", "PATCH"])
def VariableHandler(request: Request):
    match request.method:
        case "GET":
            handler_id = int(request.query_params.get('id'))
            data = []
            try:
                vars = Variable.objects.filter(profile_id=handler_id).all()
                for var in vars:
                    data.append({
                        "name": var.name,
                        "value": var.value,
                    })
                return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
            except:
                return JsonResponse({"error": True, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        
        case "POST":
            data = request.data
            print(data)
            try:
                var = Variable.objects.create(
                    profile_id=int(data["profile_id"]),
                    name=data["name"],
                    value=data["value"]
                )
                return JsonResponse({"error": False, "message": "Success"}, status=status.HTTP_200_OK, safe=False)
            except:
                return JsonResponse({"error": True, "message": "Failed"}, status=status.HTTP_400_BAD_REQUEST, safe=False)
        
        case "PATCH":
            data = request.data
            try:
                var = Variable.objects.filter(profile_id=int(data["profile_id"])).filter(name=data["name"]).first()
                var.value = data["value"]
                var.save()
                return JsonResponse({"error": False, "message": "Success"}, status=status.HTTP_200_OK, safe=False)
            except:
                return JsonResponse({"error": True, "message": "Failed"}, status=status.HTTP_404_NOT_FOUND, safe=False)

@api_view(["GET", "POST", "PATCH"])
def StateHandler(request: Request):
    if request.method == "GET":
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
    else:
        data = request.data
        try:
            state = StateManagment.objects.get(profile_id=int(data["profile_id"]))
            state.state = data["state"]
            state.save()
            return JsonResponse(status=status.HTTP_200_OK, data={"message": "Success"}, safe=False)
        except:
            state = StateManagment.objects.create(profile_id=int(data["profile_id"]), state=data["state"])
            dataresp = {
                "profile_id": state.profile_id,
                "state": state.state
            }
            return JsonResponse(dataresp, status=status.HTTP_201_CREATED, safe=False)