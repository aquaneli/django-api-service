from django.contrib import admin
from .models import StateManagment

# Register your models here.
@admin.register(StateManagment)
class ContentAdminStateManagment(admin.ModelAdmin):
    list_display = ["profile_id", "state"]
    