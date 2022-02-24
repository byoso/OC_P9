from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('flux/', views.flux, name="flux"),
    path('ticket_create/', views.ticket_create, name='ticket_create'),
    path(
        'review_create/<int:ticket_id>/',
        views.review_create, name='review_create'),
    path('review_publish/', views.review_publish, name='review_publish'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('unfollow/<int:id>/', views.unfollow, name='unfollow'),
]
