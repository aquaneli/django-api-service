from django.db import models

class Button(models.Model):
    caption=models.CharField(max_length=50)
    callback=models.CharField(max_length=50, blank=True, null=True)
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
        ('clbck', 'callback'),
    ]
    cont=models.CharField(max_length=100)
    type=models.CharField(max_length=10, choices=TypeChoises, default='cmd')
    
    class Meta:
        verbose_name = 'Триггер'
        verbose_name_plural = 'Триггеры'
        
    def __str__(self):
        return self.cont

class Condition(models.Model):
    logic = [
        ('=', 'равно'),
        ('!=', 'не равно'),
        ('>', 'больше'),
        ('<', 'меньше'),
    ]
    caption = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)
    operation = models.CharField(max_length=5, choices=logic, default='=')
    value = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'
        
    def __str__(self):
        return self.caption

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    trigger = models.ForeignKey(Trigger, on_delete=models.SET_NULL, default=None, null=True) 
    kb=models.ForeignKey(Keyboard, on_delete=models.SET_NULL, blank=True, null=True)
    state=models.CharField(max_length=100, blank=True, null=True)
    next_state=models.CharField(max_length=100, blank=True, null=True)
    conditions=models.ManyToManyField(Condition, blank=True, related_name='conditions')
    set_variable=models.CharField(max_length=100, blank=True, null=True)
    set_value=models.CharField(max_length=100, blank=True, null=True)
    next_msg=models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    delay=models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
    def __str__(self):
        return self.answer

class MessageGroup(models.Model):
    name=models.CharField(max_length=100)
    messages=models.ManyToManyField(Answer, blank=True, related_name='group')
    
    class Meta:
        verbose_name = 'Группа сообщений'
        verbose_name_plural = 'Группы сообщений'
        
    def __str__(self):
        return self.name