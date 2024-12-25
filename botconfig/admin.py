from django.contrib import admin
from .models import BotConfig
# Register your models here.
@admin.register(BotConfig)
class BotAdmin(admin.ModelAdmin):
    list_display = ["caption", "token"]
    