from django.shortcuts import render, redirect
from django import reverse
from django.contrib.auth import authenticate, login

def login_view(request):
    redirect_url = reverse('main_page')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html')

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    pass 

# Create your views here.
