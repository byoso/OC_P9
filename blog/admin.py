from dataclasses import field
from django.contrib import admin
from .models import (
    Ticket,
    Review,
    UserFollows
)


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ('title', 'user', 'description')


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('ticket', 'user')


class UserFollowsAdmin(admin.ModelAdmin):
    model = UserFollows
    list_display = ('user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
