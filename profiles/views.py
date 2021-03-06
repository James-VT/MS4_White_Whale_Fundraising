""" Views for the profile app """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from donations.models import Donation
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Displays the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)
    donations = profile.donations.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'donations': donations,
    }

    return render(request, template, context)


def donation_history(request, donation_number):
    """ Displays the user's donation history """
    donation = get_object_or_404(Donation, donation_number=donation_number)

    messages.info(request, (
        f'This is a past confirmation for donation number {donation_number}.'
    ))

    template = 'donations/donation_success.html'
    context = {
        'donation': donation,
        'from_profile': True,
        'donation_gift_aid': float(donation.donation_total)*1.25,
    }

    return render(request, template, context)
