from django.urls import path

from .views import ArticleCreate, ArticleList, ArticleView

urlpatterns = [
    path('create/', ArticleCreate.as_view(), name='create_article'),
    path('all/', ArticleList.as_view() , name='archive'),
    path('<int:pk>', ArticleView.as_view() , name='article_info'),
]