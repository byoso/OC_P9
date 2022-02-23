from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from project_LITReview import const


def login_page(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                messages.add_message(
                    request, messages.SUCCESS, f"Bienvenue {user.username}.",
                    extra_tags=const.SUCCESS
                    )
                login(request, user)
                return redirect('flux')
            else:
                messages.add_message(
                    request, messages.ERROR, (
                        "Aucun utilisateur ne correspond à ce nom ou ce"
                        " mot de passe"
                        ),
                    extra_tags=const.ERROR
                )

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
            return redirect('flux')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(
                            request, messages.ERROR, (
                                error
                                ),
                            extra_tags=const.ERROR
                        )

    form = forms.SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "authentication/signup_page.html", context)
