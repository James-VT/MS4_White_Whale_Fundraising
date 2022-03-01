""" Views for our donation pages """
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DonationForm
from .models import Donation


def donation_form(request):
    """ Donation form page """
    form = DonationForm
    return render(request, 'donations/donation_form.html', {'donation_form': form})


def donate(request):
    """ View for taking payment """

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
            'county': request.POST['county']
        }

        if request.POST['donation_custom'] >= 1:
            donation_total = request.POST['donation_custom']
            'donation_total': donation_total
        elif request.POST['donation_selectors'] >= 1:
            donation_total = request.POST['donation_selectors']
            'donation_total': donation_total
        else:
            return redirect(reverse())

        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))


def success_msg(request, args):
    """ Success page """
    amount = args
    return render(request, 'donations/donation_success.html', {'amount': amount})
