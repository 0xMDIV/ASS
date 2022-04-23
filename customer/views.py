from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib import messages


from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm
    return render(request, 'customer/signup.html', {
        'form': form
    })


def log_in(request):
    error = False
    if request.user.is_authenticated:
        messages.info(request, 'Du bist bereits eingeloggt')
        return redirect(reverse('index'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'customer/login.html', {
        'form': form,
        'error': error
    })


def log_out(request):
    logout(request)
    print('logged out')
    return redirect(reverse('index'))