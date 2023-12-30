from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context ={}
                return render(request, 'chatPage.html', context)


    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})