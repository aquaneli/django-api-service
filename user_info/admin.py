from django.contrib import admin
from .models import Profile, UserProfile

# Register your models here.

@admin.register(Profile)
class ContentAdminProfile(admin.ModelAdmin):
    list_display = ["active", "is_admin"]
    # list_filter = ["statuses", "is_admin"]

@admin.register(UserProfile)
class ContentAdminUserProfile(admin.ModelAdmin):
    list_display = ["name", "username", "city", "pswdhache", "profile"]
    