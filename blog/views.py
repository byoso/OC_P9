from itertools import chain
from webbrowser import get

from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import (
    Ticket,
    Review,
    UserFollows,
)
from .forms import (
    TicketCreateForm,
    ReviewCreateForm,
    SearchForm,
)
from project_LITReview import const


def home(request):
    return render(request, 'blog/home.html')


@login_required
def flux(request):
    reviews = request.user.get_reviews()
    tickets = request.user.get_tickets()
    reviewes_for_tickets = Review.objects.filter(ticket__user=request.user)

    posts = sorted(
        chain(
            reviews,
            tickets,
            reviewes_for_tickets,
            ),
        key=lambda post: post.time_created, reverse=True)
    context = {
        "posts": posts,
    }
    return render(request, "blog/flux.html", context)


@login_required
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
    if ticket.reviewed:
        raise Http404()
    if request.method == "POST":
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            ticket.reviewed = True
            ticket.save()
            return redirect('flux')

    form = ReviewCreateForm()
    context = {
        "ticket": ticket,
        "form": form,
    }
    return render(request, "blog/review_create.html", context)


@login_required
def review_publish(request):
    """Create à spontaneous review without ticket"""
    if request.method == "POST":
        ticket_form = TicketCreateForm(request.POST, request.FILES)
        review_form = ReviewCreateForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            ticket.reviewed = True
            ticket.save()
            return redirect('flux')

    ticket_form = TicketCreateForm()
    review_form = ReviewCreateForm()
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, "blog/review_publish.html", context)


@login_required
def subscriptions(request):
    followings = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['entry']
            try:
                user_to_follow = get_user_model().objects.get(username=name)
            except get_user_model().DoesNotExist:
                messages.add_message(
                    request, messages.ERROR, (
                        f"Il n'existe pas d'utilisateur \"{name}\""
                        ),
                    extra_tags=const.ERROR
                )
                return redirect('subscriptions')
            else:
                new_follow = UserFollows(
                    user=request.user, followed_user=user_to_follow)
                new_follow.save()
                messages.add_message(
                    request, messages.SUCCESS, (
                        f"Vous êtes abonné à \"{name}\""
                        ),
                    extra_tags=const.SUCCESS
                )
                return redirect('subscriptions')

    form = SearchForm()
    context = {
        'followings': followings,
        'followers': followers,
        'form': form,
    }
    return render(request, 'blog/subscriptions.html', context)


@login_required
def unfollow(request, id):
    unfollow = get_object_or_404(get_user_model(), id=id)
    if request.method == "POST":
        unfollowing = get_object_or_404(
            UserFollows, user=request.user, followed_user=unfollow)
        print(unfollowing)
        unfollowing.delete()
        messages.add_message(
            request, messages.SUCCESS, (
                f"Vous vous êtes désabonné à \"{unfollow.username}\""
                ),
            extra_tags=const.SUCCESS
        )
        return redirect('subscriptions')

    context = {
        "unfollow": unfollow,
    }
    return render(request, 'blog/unfollow.html', context)


@login_required
def posts(request):
    reviews = request.user.get_reviews()
    tickets = request.user.get_tickets()
    posts = sorted(
        chain(
            reviews,
            tickets,
            ),
        key=lambda post: post.time_created, reverse=True)
    context = {
        'posts': posts,
    }
    return render(request, "blog/posts.html", context)


@login_required
def post_delete(request, type, id):
    if type == 'review':
        post = get_object_or_404(Review, id=id)
        ticket = post.ticket
        ticket.reviewed = False
        ticket.save()
    elif type == 'ticket':
        post = get_object_or_404(Ticket, id=id)
    else:
        raise Http404()
    if request.method == "POST":
        post.delete()
        return redirect('posts')
    context = {
        'post': post,
        'type': type,
    }
    return render(request, 'blog/post_delete.html', context)


@login_required
def post_update(request, type, id):
    if request.method == "POST":
        if type == 'review':
            post = get_object_or_404(Review, id=id)
            form = ReviewCreateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
        elif type == 'ticket':
            post = get_object_or_404(Ticket, id=id)
            form = TicketCreateForm(
                request.POST, request.FILES, instance=post)
            reviewed = post.reviewed
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.reviewed = reviewed
                ticket.save()
        else:
            raise Http404()
        return redirect('posts')

    if type == 'review':
        post = get_object_or_404(Review, id=id)
        form = ReviewCreateForm(instance=post)

    elif type == 'ticket':
        post = get_object_or_404(Ticket, id=id)
        form = TicketCreateForm(instance=post)
    else:
        raise Http404()

    context = {
        'post': post,
        'form': form,
        'type': type,
    }
    return render(request, 'blog/post_update.html', context)
