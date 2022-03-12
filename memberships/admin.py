""" Registers the membership models for the site admin """
from django.contrib import admin
from .models import Membership


admin.site.register(Membership)
