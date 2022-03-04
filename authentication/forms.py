from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


"""The forms here are customized to match with the bulma css framework
"""


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe",
        max_length=150, required=True,
        widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        max_length=150, required=True,
        widget=forms.PasswordInput(attrs={'class': 'input'}))

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
        required=True,
        widget=forms.TextInput(
            attrs={"class": "input"}))
    password = forms.CharField(
        max_length=150, label="Mot de passe",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "input"}))
