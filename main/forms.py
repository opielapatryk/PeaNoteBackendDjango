from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'FIRST NAME'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'LAST NAME'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'PASSWORD'})
        self.fields['password2'].widget.attrs.update({'placeholder':'PASSWORD CONFIRMATION'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))

    error_messages = {
        "invalid_login": (
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }