from django.urls import path

from .views import ArticleCreate, ArticleList, index

urlpatterns = [
    path('create/', ArticleCreate.as_view(), name='create_article'),
    path('', ArticleList.as_view() , name='archive')
]