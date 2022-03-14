""" URLs for sponsorship """
from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_sponsorship, name="add_sponsorship"),
    path('sponsorship_success/<sponsorship_number>', views.sponsorship_success, name="sponsorship_success"),
]
