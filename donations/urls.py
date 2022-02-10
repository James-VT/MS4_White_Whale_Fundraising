from django.urls import path
from . import views

urlpatterns = [
    path('donation_success/', views.success_msg, name="donation_success"),
]
