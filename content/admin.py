from django.contrib import admin
from .models import Keyboard, Button
from .models import Status, Answer, Trigger

# Register your models here.
@admin.register(Keyboard)
class ContentAdminKeyboard(admin.ModelAdmin):
    list_display = ["type"]
    
@admin.register(Button)
class ContentAdminButton(admin.ModelAdmin):
    list_display = ["caption", "callback"]
    
@admin.register(Status)
class ContentAdminStatus(admin.ModelAdmin):
    list_display = ["caption"]
    
@admin.register(Answer)
class ContentAdminAnswer(admin.ModelAdmin):
    list_display = ["id", "answer", "kb" ,"trigger", "state", "next_state"]
    
@admin.register(Trigger)
class ContentAdminTrigger(admin.ModelAdmin):
    list_display = ["cont", "type"]