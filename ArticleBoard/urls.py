from django.urls import path

from .views import ArticleCreate, index

urlpatterns = [
    path('create/', ArticleCreate.as_view(), name='create_article'),
    path('', index, name='index')
]