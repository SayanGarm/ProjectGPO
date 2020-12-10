from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView, PasswordResetDoneView

from .views import UserPage, ModeratorPage, StartPageSwitch, UsersListPage, UserProfilePage


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', StartPageSwitch ,name='start-page-switch'),
    path('customers/', UsersListPage.as_view() ,name='customers'),
    path('customer/<int:pk>/', UserProfilePage.as_view(), name="customer"),

    path(
        'reset_password/', 
        PasswordResetView.as_view(template_name="reset_pass/password_reset.html"),
        name="reset_password"
    ),
    path(
        'reset_password_sent/',
        PasswordResetDoneView.as_view(template_name="reset_pass/password_reset_sent.html"),
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name="reset_pass/password_reset_form.html"),
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/',
        PasswordResetCompleteView.as_view(template_name="reset_pass/password_reset_done.html"),
        name="password_reset_complete"
    ),
]