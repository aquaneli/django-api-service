from django.db import models

class StateManagment(models.Model):
    profile_id=models.IntegerField()
    state=models.CharField(max_length=100)
   
    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
         
    def __str__(self):
        return self.state

class Variable(models.Model):
    name=models.CharField(max_length=100)
    value=models.CharField(max_length=100)
    profile_id=models.IntegerField()
    class Meta:
        verbose_name = 'Переменная'
        verbose_name_plural = 'Переменные'
    def __str__(self):
        return self.name