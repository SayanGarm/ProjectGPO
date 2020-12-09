from django.db import models
from django.contrib.auth.models import User

class ArticleManager(models.Manager):
    def getAllFromRole(self, user):
        groups = user.groups
        if (groups.filter(name = 'moderator').exists()):
            return self.all()
        if (groups.filter(name = 'customer').exists()):
            return self.filter(author=user)


STATUS = ( ('A', 'Проверена'),
        ('B', 'Требует исправлений'),
        ('C', 'Ожидает проверки') )

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name='Автор')
    document = models.FileField(verbose_name='Документ')

    status = models.CharField(max_length=20, default='C', choices=STATUS, verbose_name='Статус')

    objects = ArticleManager()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.document.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-published']

class Review(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    content = models.TextField(null=True, blank=True, verbose_name='Текст рецензии')

    status = models.CharField(max_length=20, default='C', choices=STATUS, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Рецензии'
        verbose_name = 'Рецензия'
        ordering = ['-published']