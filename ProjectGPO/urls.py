from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('article/', include('ArticleBoard.urls'), name='main'),
    path('admin/', admin.site.urls)
]
