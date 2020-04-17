from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.index, name="trang chu"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="polls/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]