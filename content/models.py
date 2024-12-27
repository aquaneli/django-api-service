from django.db import models

# Create your models here.
class Message(models.Model):
    triggers = models.CharField(max_length=100)
    buttons = models.CharField(max_length=100)
    keyboards = models.CharField(max_length=100)
    messages = models.CharField(max_length=100)
    def __str__(self):
        return f"Profile(id={self.triggers}, buttons={self.buttons}, keyboards={self.keyboards}, messages={self.messages}"

class Status(models.Model):
    caption = models.CharField(max_length=100)
    def __str__(self):
        return self.caption


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

class Trigger(models.Model):
    cont=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.cont

class Answer(models.Model):
    # id = models.IntegerField(primary_key=True)
    # type = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    class Meta:
       managed = True
    def __str__(self):
        return self.answer

# class States(models.Model):
#     id = models.IntegerField(primary_key=True)
#     phrase = models.CharField(max_length=100)
#     trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.phrase
    

# class UserProfile(models.Model):
#     id = models.IntegerField(max_length=100)
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     pswdhache = models.CharField(max_length=100)
#     profile = Profile
#     def __str__(self):
#         return self.triggers
