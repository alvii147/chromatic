from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='chromatic_app_home'),
    path('register/', views.register, name='chromatic_app_register'),
    path('login/', LoginView.as_view(template_name='chromatic_app/login.html'), name='chromatic_app_login'),
    path('logout/', LogoutView.as_view(template_name='chromatic_app/logout.html'), name='chromatic_app_logout'),
    path('upload/', views.upload, name='chromatic_app_upload'),
]