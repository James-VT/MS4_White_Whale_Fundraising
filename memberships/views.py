from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import stripe
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


@login_required
def 