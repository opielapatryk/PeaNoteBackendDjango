from django.urls import path, include
from .views import Settings, Register, Login, Friend, Friends, Index, Logout, SearchFriend, UserViewSet, StickerViewSet, get_csrf_token, CustomLoginView,CustomLogoutView, CustomRegisterView, UpdatePasswordView
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
    path("custom_login", CustomLoginView.as_view(), name="custom_login"),
    path("custom_register", CustomRegisterView.as_view(), name="custom_register"),
    path("update_password", UpdatePasswordView.as_view(), name="update_password"),
    path("friends/<int:friend_id>", login_required(Friend.as_view()), name="friend"),
    path("friends", login_required(Friends.as_view()), name="friends"),
    path("", Index.as_view(), name="index"),
    path("logout", Logout.as_view(), name="logout"),
    path('custom_logout', CustomLogoutView.as_view(), name="custom_logout"),
    path('search', login_required(SearchFriend.as_view()), name="search"),
    path('get_csrf_token/', get_csrf_token, name='get_csrf_token'),   
]