from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path("settings", login_required(views.Settings.as_view()), name="settings"),
    path("register", views.Register.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("friends/<int:user_id>", login_required(views.Friend.as_view()), name="friend"),
    path("friends", login_required(views.Friends.as_view()), name="friends"),
    path("", views.Index.as_view(), name="index"),
    path("logout", views.Logout.as_view(), name="logout"),
    path('search', login_required(views.SearchFriend.as_view()), name="search")
]