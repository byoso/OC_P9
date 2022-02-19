from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=150, widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(
        max_length=150, widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "input"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={"class": "input"}))
    password = forms.CharField(
        max_length=150, label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={"class": "input"}))
