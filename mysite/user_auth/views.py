from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'login_success.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'login_failed.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    pass


def login_page(request):
    return render(request, 'login.html')
