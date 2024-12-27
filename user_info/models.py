from django.db import models

from content.models import Status

# Create your models here.

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    registered = models.IntegerField()
    statuses = models.ManyToManyField(Status)
    last_visit = models.IntegerField()
    is_admin = models.BooleanField()
    achives = models.CharField(max_length=100)
    def __str__(self):
        return f"Profile(id={self.id}, active={self.active}, registered={self.registered}, statuses={self.statuses}, last_visit={self.last_visit}, is_admin={self.is_admin}, achives={self.achives})"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pswdhache = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
