from django.db import models

# Create your models here.

class StateManagment(models.Model):
    profile_id=models.IntegerField()
    state=models.CharField(max_length=100)
   
    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
         
    def __str__(self):
        return self.state
