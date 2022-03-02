from django import forms
from .models import (
    Ticket,
    Review,
)


class TicketNoImageCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input"}),
        label="Titre")
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "textarea",
            }),
        )

    class Meta:
        model = Ticket
        exclude = ('user', 'image')


class TicketCreateForm(TicketNoImageCreateForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            "type": "file",
        })
    )

    class Meta:
        model = Ticket
        exclude = ('user',)


class ReviewCreateForm(forms.ModelForm):
    headline = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input"}),
        label="Titre")
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "textarea",
            }),
        label="Commentaire",
        )
    CHOICES = [
        ('0', '- 0'), ('1', '- 1'), ('2', '- 2'),
        ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES,
        label="Note")

    class Meta:
        model = Review
        exclude = ('user', 'ticket',)


class SearchForm(forms.Form):
    entry = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Nom d'utilisateur",
                },
            ),
        )
