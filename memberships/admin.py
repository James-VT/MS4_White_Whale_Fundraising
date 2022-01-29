""" Registers the membership models for the site admin """
from django.contrib import admin
from .models import MembershipLevel

# Register your models here.
admin.site.register(MembershipLevel)
