from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
import authentication
from . import forms


def login_page(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
    form = forms.LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'authentication/login_page.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = forms.SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "authentication/signup_page.html", context)
