from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('settings/<int:pk>', views.AccountSettings.as_view(), name='settings'),
]