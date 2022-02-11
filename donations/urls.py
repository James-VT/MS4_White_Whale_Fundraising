""" URLs for the donation form """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_form, name="donation_form"),
    path('charge/', views.charge, name="charge"),
    path('donation_success/', views.success_msg, name="donation_success"),
]
