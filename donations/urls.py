""" URLs for the donation form """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_form, name="donation_form"),
    path('donate/', views.donate, name="donate"),
    path('donation_success/', views.success_msg, name="donation_success"),
    path('donation_fail/', views.success_msg, name="donation fail"),
]
