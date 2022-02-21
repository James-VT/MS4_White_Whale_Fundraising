""" Views for our donation pages """
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DonationForm


def donation_form(request):
    """ Donation form page """
    return render(request, 'donations/donation_form.html')


def charge(request):
    """ View for taking payment """
    amount = 0
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))


def success_msg(request, args):
    """ Success page """
    amount = args
    return render(request, 'donations/donation_success.html', {'amount': amount})
