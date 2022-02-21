from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('flux/', views.flux, name="flux"),
    path('ticket_create/', views.ticket_create, name='ticket_create'),
]
