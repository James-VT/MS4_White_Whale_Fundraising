""" Views for the sponsorship """
import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from .forms import SponsorshipForm
from .models import Sponsorship


@login_required
def add_sponsorship(request):
    """ View for taking payment and establishing a sponsorship """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        form_data = {
            'title': request.POST['title'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone_number': request.POST['phone_number'],
            'email': request.POST['email'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'gift_aid': request.POST.get('gift_aid', False),
        }

        form = SponsorshipForm(form_data)

        if form.is_valid():

            # Stripe stuff will go here, I think
            customer = stripe.Customer.create(
                email=request.POST['email'],
                name=request.POST['first_name'],
                source=request.POST['stripeToken']
            )

            request.session['save_info'] = 'saveinfo' in request.POST
            return redirect(reverse('sponsorship_success', args=[sponsorship.sponsorship_number]))
        else:
            messages.error(request, 'Your sponsorship failed')

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)

            form = SponsorshipForm(initial={
                'title': profile.default_title,
                'first_name': profile.default_first_name,
                'last_name': profile.default_last_name,
                'email': profile.default_email,
                'phone_number': profile.default_phone_number,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
                'country': profile.default_country,
                'town_or_city': profile.default_town_or_city,
                'postcode': profile.default_postcode,
            })
        except UserProfile.DoesNotExist:
            form = SponsorshipForm()
    else:
        form = SponsorshipForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your envrionment?')

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key
    }

    return render(request, 'sponsorship/sponsorship_form.html', context)


@login_required
def sponsorship_checkout(request, sponsorship_number):
    """ Confirm sponsorship view """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY
    product_id = settings.STRIPE_SPONSORSHIP_ID
    price_id = settings.STRIPE_PRICE_ID

    if request.method == "POST":

        if form.is_valid():
                add_sponsorship.sponsorship = form.save(commit=False)
                form.save()


def sponsorship_success(request, sponsorship_number):
    """
    Handles successful sponsorships
    """
    save_info = request.session.get('save_info')
    print(save_info)
    sponsorship = get_object_or_404(Sponsorship, sponsorship_number=sponsorship_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        print(profile)
        # Attaches the user's profile to the sponsorship
        sponsorship.user_profile = profile
        sponsorship.save()

        # Save the user's submitted info
        if save_info:
            profile_data = {
                'default_title': sponsorship.title,
                'default_first_name': sponsorship.first_name,
                'default_last_name': sponsorship.last_name,
                'default_email': sponsorship.email,
                'default_phone_number': sponsorship.phone_number,
                'default_country': sponsorship.country,
                'default_postcode': sponsorship.postcode,
                'default_town_or_city': sponsorship.town_or_city,
                'default_street_address1': sponsorship.street_address1,
                'default_street_address2': sponsorship.street_address2,
                'default_county': sponsorship.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Sponsorship successfully set up! \
        Your sponsorship number is {sponsorship_number}. A confirmation \
        email will be sent to {sponsorship.email}.')

    template = 'sponsorship/sponsorship_success.html'
    context = {
        'sponsorship': sponsorship,
        'sponsorship_gift_aid': float(sponsorship.sponsorship_total)*1.25,
    }

    return render(request, template, context)
