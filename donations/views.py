""" Views for our donation pages """
from django.shortcuts import (render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
import stripe
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from .forms import DonationForm
from .models import Donation


# This view should be able to handle anything to do with adding a donation
# It might help you make sense of what's happening by giving it a name such as 'AddDonation'
# It will be responsible for processing either POST (when form is submitted), or GET (when user
# visits the page to see the form)
def add_donation(request):
    """ View for taking payment and saving the donation to the database """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
            'donation_total': request.POST['donation_total']
        }
        # Instantiate the form and populate with above data using:
        form = DonationForm(form_data)

        # Check that the form is valid using:
        if form.is_valid():
            donation = form.save(commit=False)
            form.save()

            # Save user's info to their profile if it's all good here
            request.session['save_info'] = 'save-info' in request.POST
            print(form_data)
            print('Data:', request.POST)
            return redirect(reverse('donation_success', args=[donation.donation_number]))
        else:
            print('Not valid')
            print(form.errors)
            messages.error(request, 'Your donation failed')

        # ^^ this should be everything you need to save a donation
        # once the form is submitted. Add a return statement to send
        # user to another path etc.

    # At this level, we're outside the POST block, so we can instantiate
    # a blank form using:

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)

            form = DonationForm(initial={
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
            form = DonationForm()
    else:
        form = DonationForm()

    # ^^ Could then pass this form in as context to whatever we render. Then
    # in the template we'll have access to 'form', which can be rendered using:
    # {{ form }}

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        # 'client_secret': intent.client_secret,
    }

    return render(request, 'donations/donation_form.html', context)
    # return redirect(reverse('success', args=[donation_total]))
    # ^^ this should be a return render of the donation_form template


def donation_success(request, donation_number):
    """
    Handles successful donations
    """
    save_info = request.session.get('save_info')
    print(save_info)
    donation = get_object_or_404(Donation, donation_number=donation_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        print(profile)
        # Attaches the user's profile to the donation
        donation.user_profile = profile
        donation.save()

        # Save the user's submitted info
        if save_info:
            profile_data = {
                'default_title': donation.title,
                'default_first_name': donation.first_name,
                'default_last_name': donation.last_name,
                'default_email': donation.email,
                'default_phone_number': donation.phone_number,
                'default_country': donation.country,
                'default_postcode': donation.postcode,
                'default_town_or_city': donation.town_or_city,
                'default_street_address1': donation.street_address1,
                'default_street_address2': donation.street_address2,
                'default_county': donation.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Donation successfully processed! \
        Your donation number is {donation_number}. A confirmation \
        email will be sent to {donation.email}.')

    template = 'donations/donation_success.html'
    context = {
        'donation': donation,
        'donation_gift_aid': float(donation.donation_total)*1.25,
    }

    return render(request, template, context)
