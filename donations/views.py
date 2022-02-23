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

        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))


def success_msg(request, args):
    """ Success page """
    amount = args
    return render(request, 'donations/donation_success.html', {'amount': amount})
