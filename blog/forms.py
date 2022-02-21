from django import forms
from .models import (
    Ticket,
    Review,
    UserFollows
)


class TicketCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input"}),
        label="Titre")
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "textarea",
            }),
        )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            "type": "file",
        })
    )


    class Meta:
        model = Ticket
        exclude = ('user',)
