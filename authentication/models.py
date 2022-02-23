from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Review, Ticket


class User(AbstractUser):

    def get_reviews(self):
        reviews = Review.objects.filter(user=self)
        return reviews

    def get_tickets(self):
        tickets = Ticket.objects.filter(user=self)
        return tickets
