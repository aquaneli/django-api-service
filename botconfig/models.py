from django.db import models

# Create your models here.
class BotConfig (models.Model):
    caption = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    def __str__(self):
        return self.caption