from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import User, Sticker
from .forms import LoginForm, RegisterForm 
from rest_framework import viewsets
from .serializer import UserSerializer, StickerSerialzier
from django.views import generic 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("login"))
        return super().dispatch(request, *args, **kwargs)

class Logout(LogoutView):
    next_page = 'login'

class Register(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

class Settings(TemplateView):
    template_name = 'settings.html'

class Friend(TemplateView):
    template_name = 'friend.html'

class Friends(ListView):
    template_name = 'friends.html'
    model = User

    def get_queryset(self):
        queryset = self.request.user.friends.all()
        return queryset 
    

class SearchFriend(ListView):
    template_name = 'search.html'
    model = User

    def get_queryset(self):
        email = self.request.GET.get('email')
        queryset = User.objects.filter(is_active=True)

        queryset = queryset.filter(email=email)
        return queryset 
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StickerViewSet(viewsets.ModelViewSet):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerialzier