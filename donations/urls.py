""" URLs for the donation form """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_donation, name="add_donation"),
    path('donation_success/<donation_number>', views.donation_success, name="donation_success"),
]
