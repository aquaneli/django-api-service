from django.contrib import admin
from .models import Message
from .models import Profile, Status, Answer, Trigger

# Register your models here.
@admin.register(Message)
class ContentAdminMessage(admin.ModelAdmin):
    list_display = ["triggers", "buttons", "keyboards", "messages"]
    
@admin.register(Status)
class ContentAdminStatus(admin.ModelAdmin):
    list_display = ["caption"]

@admin.register(Profile)
class ContentAdminProfile(admin.ModelAdmin):
    list_display = ["active", "is_admin"]
    # list_filter = ["statuses", "is_admin"]
    
@admin.register(Answer)
class ContentAdminAnswer(admin.ModelAdmin):
    list_display = ["id", "answer", "trigger"]
    
@admin.register(Trigger)
class ContentAdminTrigger(admin.ModelAdmin):
    list_display = ["cont", "type"]