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

