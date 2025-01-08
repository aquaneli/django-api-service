from django.contrib import admin
from .models import Profile, UserProfile, Status, Achive

# Register your models here.

@admin.register(Status)
class ContentAdminStatus(admin.ModelAdmin):
    list_display = ["caption"]

@admin.register(Profile)
class ContentAdminProfile(admin.ModelAdmin):
    list_display = ["tgid", "active", "is_admin"]
    list_filter = ["active", "is_admin", "statuses"]

@admin.register(UserProfile)
class ContentAdminUserProfile(admin.ModelAdmin):
    list_display = ["name", "username", "city", "pswdhache", "profile"]

@admin.register(Achive)
class ContentAdminAchive(admin.ModelAdmin):
    list_display = ["caption"]