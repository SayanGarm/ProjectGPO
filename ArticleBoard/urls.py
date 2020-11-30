from django.urls import path

from .views import index

urlpatterns = [
    path('create/', index, name='create_article'),
]