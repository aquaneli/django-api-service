from rest_framework.decorators import api_view
import rest_framework

from django.http.response import JsonResponse
import rest_framework.request

from .serializers import BotConfigSerializer
from .models import BotConfig

@api_view(["GET"])
def GetBotHandler(request: rest_framework.request):
    bot_caption = request.query_params.get('caption', 'default')
    token = ""
    try:
        bot = BotConfig.objects.get(caption=bot_caption)
        token = bot.token
    except: pass

    return JsonResponse(token, safe=False)