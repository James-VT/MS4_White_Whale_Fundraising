from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import stripe
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.views.generic import ListView
from .models import Membership, UserMembership, Subscription


def get_user_membership(request):
    """ Checks if the user is a member """
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


class MembershipSelectView(ListView):
    model = Membership
