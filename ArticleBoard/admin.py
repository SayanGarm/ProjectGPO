from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_display_links = ('title', 'author')


admin.site.register(Article, ArticleAdmin)