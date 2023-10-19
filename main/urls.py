from django.urls import path
from . import views

urlpatterns = [
    path("settings", views.Settings.as_view(), name="settings"),
    path("register", views.Register.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("friends/<int:user_id>", views.Friend.as_view(), name="friend"),
    path("friends", views.Friends.as_view(), name="friends"),
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path('search', views.SearchFriend.as_view(), name="search")
]