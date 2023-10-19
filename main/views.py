from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from main.models import User
from .forms import LoginForm, RegisterForm
from django.views import generic 
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.views.generic import TemplateView

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context={})
    else:
        return HttpResponseRedirect(reverse("login"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

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

    # def get_queryset(self):
    #     queryset = self.model.objects.all()
    #     search_query = self.request.GET.get('q')
    #     if search_query:
    #         queryset = queryset.filter(email__icontains=search_query)
    #     return queryset

    # Query for requested email
    # try:
    #     email = Email.objects.get(user=request.user, pk=email_id)
    # except Email.DoesNotExist:
    #     return JsonResponse({"error": "Email not found."}, status=404)

    # # Return email contents
    # if request.method == "GET":
    #     return JsonResponse(email.serialize())

    # # Update whether email is read or should be archived
    # elif request.method == "PUT":
    #     data = json.loads(request.body)
    #     if data.get("read") is not None:
    #         email.read = data["read"]
    #     if data.get("archived") is not None:
    #         email.archived = data["archived"]
    #     email.save()
    #     return HttpResponse(status=204)

    # # Email must be via GET or PUT
    # else:
    #     return JsonResponse({
    #         "error": "GET or PUT request required."
    #     }, status=400)