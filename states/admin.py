from django.contrib import admin
from .models import StateManagment, Variable

# Register your models here.
@admin.register(StateManagment)
class ContentAdminStateManagment(admin.ModelAdmin):
    list_display = ["profile_id", "state"]

@admin.register(Variable)
class ContentAdminVariable(admin.ModelAdmin):
    list_display = ["name", "value", "profile_id"]
    list_filter = ["name", "value", "profile_id"]