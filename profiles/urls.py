""" Contains the URLs for the profile app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('donation_history/<donation_number>', views.donation_history, name='donation_history'),
]
