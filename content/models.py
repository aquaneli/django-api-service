from django.db import models

# Create your models here.


class Button(models.Model):
    caption=models.CharField(max_length=50)
    callback=models.CharField(max_length=50)

class Keyboard(models.Model):
    type = models.CharField(max_length=10)
    buttons=models.ManyToManyField(Button)

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
    answer = models.CharField(max_length=100)
    trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    kb=models.ForeignKey(Keyboard, on_delete=models.SET_NULL, blank=True, null=True)
    state=models.CharField(max_length=100)
    next_state=models.CharField(max_length=100)
    class Meta:
       managed = True
    def __str__(self):
        return self.answer

