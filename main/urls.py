from django.urls import path
from . import views

urlpatterns = [
    path("settings", views.settings, name="settings"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("friends/<int:user_id>", views.friend, name="friend"),
    path("friends", views.friends, name="friends"),
    path("", views.index, name="index"),
]