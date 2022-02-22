from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import (
    Ticket,
)
from .forms import (
    TicketCreateForm,
    ReviewCreateForm,
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


@login_required
def review_create(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux')

    form = ReviewCreateForm()
    context = {
        "ticket": ticket,
        "form": form,
    }
    return render(request, "blog/review_create.html", context)
