""" Views for our donation pages """
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import DonationForm
from .models import Donation


# This view appears unnecessary and doesn't have enough in it to
# successfully store info in the DB
# def donation_form(request):
#     """ Donation form page """
#     form = DonationForm()
#     return render(request, 'donations/donation_form.html', {'donation_form': form})


# This view should be able to handle anything to do with adding a donation
# It might help you make sense of what's happening by giving it a name such as 'AddDonation'
# It will be responsible for processing either POST (when form is submitted), or GET (when user
# visits the page to see the form)
def add_donation(request):
    """ View for taking payment and saving the donation to the database """

    if request.method == 'POST':
        # So this is what the view should do when form is submitted (POSTed)
        # donation_custom = int(request.POST['donation_custom'])
        # donation_selectors = request.POST['donation_selectors']
        # print(donation_custom)
        # print(type(donation_custom))
        # print(donation_selectors)
        # if request.POST['donation_custom'] != '':
        #     donation_custom = request.POST['donation_custom']
        #     print(donation_custom)
        #     print(type(donation_custom))
        #     donation_total = float(request.POST['donation_custom'])
        #     print(donation_total)
        #     print(type(donation_total))
        # donation_selectors = request.POST.get('donation_selectors', '')
        # if donation_selectors:
        #     donation_selectors = request.POST['donation_selectors']
        #     print(donation_selectors)
        #     print(type(donation_selectors))
        #     donation_total = float(request.POST['donation_selectors'])
        #     print(donation_total)
        #     print(type(donation_total))
        # form_data is what we can use to populate an instance of the DonationForm
        # donation_total_uncleaned = request.POST['donation_total']
        # donation_total = donation_total_uncleaned[1:]
        # donation_value = request.POST['donation_total'][1]
        # print(donation_value)
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
            form.save()
        else:
            print('Not valid')
            print(form.errors)
            messages.error(request, 'Your donation failed')

        # ^^ this should be everything you need to save a donation
        # once the form is submitted. Add a return statement to send
        # user to another path etc.
        print(form_data)

        print('Data:', request.POST)

    # At this level, we're outside the POST block, so we can instantiate
    # a blank form using:
    form = DonationForm()

    # ^^ Could then pass this form in as context to whatever we render. Then
    # in the template we'll have access to 'form', which can be rendered using:
    # {{ form }}

    return render(request, 'donations/donation_form.html', {'form': form})
    # return redirect(reverse('success', args=[donation_total]))
    # ^^ this should be a return render of the donation_form template


def success_msg(request, args):
    """ Success page """
    amount = args
    return render(request, 'donations/donation_success.html', {'amount': amount})
