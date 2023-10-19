from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from main.models import User
from .forms import LoginForm, RegisterForm
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

class SearchFriend(ListView):
    template_name = 'search.html'
    model = User

    def get_queryset(self):
        email = self.request.GET.get('email')
        queryset = User.objects.filter(is_active=True)
        if email:
            queryset = queryset.filter(email=email)
        return queryset 