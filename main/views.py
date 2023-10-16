from django.shortcuts import render

# your board
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context={})
    else:
        return render(request, 'login.html', context={})

# login page
def login(request):
    return render(request, 'login.html', context={})

# register page
def register(request):
    return render(request, 'register.html', context={})

# settings
def settings(request):
    return render(request, 'settings.html', context={})

# your friend board
def friend(request):
    return render(request, 'friend.html', context={})

# list your friends
def friends(request):
    return render(request, 'friends.html', context={})