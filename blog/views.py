from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (
    Ticket,
)
from .forms import (
    TicketCreateForm,
)


def home(request):
    context = {

    }
    return render(request, 'blog/home.html', context)


@login_required
def flux(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets,
    }
    return render(request, "blog/flux.html", context)


def ticket_create(request):
    if request.method == "POST":
        form = TicketCreateForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    form = TicketCreateForm()
    context = {
        "form": form,
    }
    return render(request, "blog/ticket_create.html", context)
