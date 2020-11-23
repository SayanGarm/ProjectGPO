from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name='Автор')
    document = models.FileField()
    
    def delete(self, *args, **kwargs):
        self.document.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-published']