from django.urls import path, include
from .views import Settings, Register, Login, Friend, Friends, Index, Logout, SearchFriend, UserViewSet, StickerViewSet
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stickers', StickerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("settings", login_required(Settings.as_view()), name="settings"),
    path("register", Register.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    path("friends/<int:friend_id>", login_required(Friend.as_view()), name="friend"),
    path("friends", login_required(Friends.as_view()), name="friends"),
    path("", Index.as_view(), name="index"),
    path("logout", Logout.as_view(), name="logout"),
    path('search', login_required(SearchFriend.as_view()), name="search"),
    
]