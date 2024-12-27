from django.contrib import admin
from .models import Message
from .models import Status, Answer, Trigger

# Register your models here.
@admin.register(Message)
class ContentAdminMessage(admin.ModelAdmin):
    list_display = ["triggers", "buttons", "keyboards", "messages"]
    
@admin.register(Status)
class ContentAdminStatus(admin.ModelAdmin):
    list_display = ["caption"]
    
@admin.register(Answer)
class ContentAdminAnswer(admin.ModelAdmin):
    list_display = ["id", "answer", "trigger"]
    
@admin.register(Trigger)
class ContentAdminTrigger(admin.ModelAdmin):
    list_display = ["cont", "type"]