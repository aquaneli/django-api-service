from django.contrib import admin
from .models import Step

# Register your models here.

@admin.register(Step)
class ContentAdminStep(admin.ModelAdmin):
    list_display = ["profile_id", "state"]