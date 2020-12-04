from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('register', views.register),
    path('link', views.link),
    path('help', views.help),
    path('logout', views.logout)
]
