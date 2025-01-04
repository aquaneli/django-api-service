from django.db import models

# Create your models here.

class Status(models.Model):
    caption = models.CharField(max_length=100)
    def __str__(self):
        return self.caption

class Profile(models.Model):
    tgid = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    registered = models.DateTimeField(null=True, blank=True)
    statuses = models.ManyToManyField(Status, blank=True)
    last_visit = models.DateTimeField(auto_created=True , auto_now=True)
    is_admin = models.BooleanField()
    achives = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"Profile(id={self.tgid}, active={self.active}, registered={self.registered}, statuses={self.statuses}, last_visit={self.last_visit}, is_admin={self.is_admin}, achives={self.achives})"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pswdhache = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
