from django.urls import path
from . import views

urlpatterns = [
    path("settings", views.settings, name="settings"),
    path("register", views.Register.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("friends/<int:user_id>", views.friend, name="friend"),
    path("friends", views.friends, name="friends"),
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
]