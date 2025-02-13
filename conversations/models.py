from django.db import models

# Create your models here.

# сделать можели евентс 
# id пользвоателя
# Наименоание события 
# Тип события 
# Текс события


class Event(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    text = models.TextField()