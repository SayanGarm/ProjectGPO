from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    first_name = models.CharField(max_length=20,null=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=20,null=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=20,null=True, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email-адрес')
    
    bio = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'