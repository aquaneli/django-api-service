from django.db import models

# Create your models here.

class Step(models.Model):
    profile_id=models.IntegerField()
    state=models.CharField(max_length=100)
    def __str__(self):
        return self.state
