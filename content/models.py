from django.db import models

# Create your models here.


class Button(models.Model):
    caption=models.CharField(max_length=50)
    callback=models.CharField(max_length=50)
    row=models.IntegerField(default=0)
    order=models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'
        
    def __str__(self):
        return self.caption

class Keyboard(models.Model):
    TypeChoises = [
        ('inline', 'inline'),
        ('reply', 'reply'),
    ]
    caption = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TypeChoises, default='reply')
    buttons=models.ManyToManyField(Button)
    
    class Meta:
        verbose_name = 'Клавиатура'
        verbose_name_plural = 'Клавиатуры'
        
    def __str__(self):
        return self.caption

class Status(models.Model):
    caption = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        
    def __str__(self):
        return self.caption

class Trigger(models.Model):
    TypeChoises = [
        ('cmd', 'cmd'),
        ('text', 'text'),
    ] 
    cont=models.CharField(max_length=100)
    type=models.CharField(max_length=5, choices=TypeChoises, default='cmd')
    
    class Meta:
        verbose_name = 'Триггер'
        verbose_name_plural = 'Триггеры'
        
    def __str__(self):
        return self.cont

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    kb=models.ForeignKey(Keyboard, on_delete=models.SET_NULL, blank=True, null=True)
    state=models.CharField(max_length=100)
    next_state=models.CharField(max_length=100)
    next_msg=models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    delay=models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
    def __str__(self):
        return self.answer

