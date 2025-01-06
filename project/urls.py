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
from content.views import GetTextAnswerHandler 
from user_info.views import ProfileHandler
from content.views import GetCMDAnswerHandler
from states.views import StateHandler



admin.site.site_header = 'Администрирование бота'
admin.site.index_title = 'Система менеджмента сообщений'
admin.site.site_title = 'Bot Content Managment System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('answers/txt/', GetTextAnswerHandler),
    path('profiles/', ProfileHandler),
    # path('profiles/save/', POSTProfileHandler),
    path('answers/cmd/', GetCMDAnswerHandler),
    # path('states/update/', POSTStateHandler),
    path('states/', StateHandler),
]

