from django.db import models

class Status(models.Model):
    caption = models.CharField(max_length=100)
    
    class Meta:
       verbose_name = 'Статус'
       verbose_name_plural = 'Статусы'
       
    def __str__(self):
        return self.caption
    
class Achive(models.Model):
    caption = models.CharField(max_length=100)
    
    class Meta:
       verbose_name = 'Достижение'
       verbose_name_plural = 'Достижения'
       
    def __str__(self):
        return self.caption

class Profile(models.Model):
    tgid = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    registered = models.DateTimeField(null=True, blank=True)
    statuses = models.ManyToManyField(Status, blank=True)
    last_visit = models.DateTimeField(auto_created=True , auto_now=True)
    is_admin = models.BooleanField()
    achives = models.ManyToManyField(Achive, blank=True)
    
    class Meta:
       verbose_name = 'Профиль'
       verbose_name_plural = 'Профили'
        
    def __str__(self):
        return str(self.tgid)

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pswdhache = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    class Meta:
       verbose_name = 'Учетная запись'
       verbose_name_plural = 'Учетные записи'
       
    def __str__(self):
        return self.name
