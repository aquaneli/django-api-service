"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from content.views import GetCMDAnswerHandler, GetTextAnswerHandler, GetAnswerHandler, GetCallbackAnswerHandler
from user_info.views import ProfileHandler, ProfileUpdateHandler
from states.views import StateHandler, VariableHandler
from botconfig.views import GetBotHandler
from conversations.views import PostCreateConversationHandler

admin.site.site_header = 'Администрирование бота'
admin.site.index_title = 'Система менеджмента сообщений'
admin.site.site_title = 'Bot Content Managment System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('answers/txt/', GetTextAnswerHandler),
    path('answers/cmd/', GetCMDAnswerHandler),
    path('answers/clb/', GetCallbackAnswerHandler), 
    path('answers/', GetAnswerHandler),
    path('variables/', VariableHandler), 
    path('profiles/lvupdate/', ProfileUpdateHandler), 
    path('profiles/', ProfileHandler),
    path('states/', StateHandler),
    path('botconfig/', GetBotHandler),
    path('conversations/', PostCreateConversationHandler),
]