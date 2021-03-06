from django.urls import path
from .views import home_view, delete_event, save_event, registration_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home_page'),
    path('delete-event/', delete_event, name='timetable-delete'),
    path('save-event/', save_event, name='timetable-save'),
    path('register/', registration_view, name='user-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),

    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
