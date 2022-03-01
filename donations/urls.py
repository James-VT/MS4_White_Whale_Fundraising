""" URLs for the donation form """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_donation, name="add_donation"),
    # path('donate/', views.donate, name="donate"),
    path('donation_success/', views.success_msg, name="donation_success"),
    path('donation_fail/', views.success_msg, name="donation fail"),
]
