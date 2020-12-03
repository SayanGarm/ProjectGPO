from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserPage, ModeratorPage, StartPageSwitch, UsersListPage


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', StartPageSwitch ,name='start-page-switch'),
    path('customers/', UsersListPage.as_view() ,name='customers'),

]