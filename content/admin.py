from django.contrib import admin
from .models import Keyboard, Button
from .models import Status, Answer, Trigger, MessageGroup

# Register your models here.
@admin.register(Keyboard)
class ContentAdminKeyboard(admin.ModelAdmin):
    list_display = ["caption", "type"]
    
@admin.register(Button)
class ContentAdminButton(admin.ModelAdmin):
    list_display = ["caption", "callback"]
    
@admin.register(Status)
class ContentAdminStatus(admin.ModelAdmin):
    list_display = ["caption"]
    
@admin.register(Answer)
class ContentAdminAnswer(admin.ModelAdmin):
    list_display = ["id", "answer", "kb" ,"trigger", "state"]
    list_filter = ["state", "trigger", "group"]
    link = "answer"
    
@admin.register(Trigger)
class ContentAdminTrigger(admin.ModelAdmin):
    list_display = ["cont", "type"]
    
@admin.register(MessageGroup) 
class ContentAdminMessageGroup(admin.ModelAdmin):
    list_display = ["name"]