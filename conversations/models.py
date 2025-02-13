from django.db import models

# Create your models here.

# сделать можели евентс 
# id пользвоателя
# Наименоание события 
# Тип события 
# Текс события

class Choise(models.Model):
    id = models.IntegerField()
    text = models.CharField(max_length=100)

class Event(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Choise, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
