from typing import Any
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
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import DeleteView
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import get_token
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import logging
from django.contrib.auth import authenticate, login, logout

class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        logger = logging.getLogger(__name__)
        logger.info(f'Login attempt - Username: {username}, Password: {password}')

        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'Authorization': 'Token ' + token.key, 'user_id':user.id})
        else:
            logger.warning(f'Login failed for username: {username}')
            return Response({'error': 'Invalid Credentials'}, status=400)
    
class CustomLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"success": "Successfully logged out"})

class Index(ListView):
    template_name = 'index.html'
    model = User

    def get_queryset(self):
        queryset = self.request.user.stickersOnBoard.all()
        return queryset

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("login"))
        return super().dispatch(request, *args, **kwargs)

class Friend(ListView):
    template_name = 'friend.html'
    model = User

    def get_queryset(self):
        user_id_from_url = self.kwargs['friend_id'] 
        user_from_url = self.model.objects.filter(id=user_id_from_url)
        queryset = user_from_url[0].stickersOnBoard.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_id = self.kwargs['friend_id']
        context['friend_id'] = User.objects.get(id=friend_id)
        return context

class Logout(LogoutView):
    next_page = 'login'

class Register(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

@method_decorator(ensure_csrf_cookie, name='dispatch')
class Login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

class Settings(TemplateView):
    template_name = 'settings.html'

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
    
@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrfToken": csrf_token})