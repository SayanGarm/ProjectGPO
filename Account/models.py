from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def get_customers(self):
        users = super().get_queryset()
        customers = []
        for user in users:
            if (user.is_customer()):
                customers.append(user)
        return customers

    def get_username(self):
        users = super().get_queryset()
        logins = []
        for user in users:
            if (user.is_customer()):
                logins.append(user.user.username)
        
        return logins

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    first_name = models.CharField(max_length=20,null=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=20,null=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=20,null=True, verbose_name='Фамилия')
    objects = ProfileManager()

    bio = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    def __str__(self):
        return self.user.username

    def is_customer(self):
        return (self.user.groups.filter(name='customer').exists())
    
    def is_moderator(self):
        return (self.user.groups.filter(name='moderator').exists())
    
    def groupExists(self):
        return self.user.groups.exists()

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'