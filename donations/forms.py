""" Donation form """
from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    """ Donation form class """

    donation_values = (('5', '£5'), ('10', '£10'), ('15', '£15'),
                       ('25', '£25'), ('50', '£50'))
    donation_selectors = forms.ChoiceField(choices=donation_values,
                                           widget=forms.RadioSelect)

    donation_custom = forms.CharField()

    class Meta:
        """ Meta class for donation form """
        model = Donation
        fields = ('title', 'first_name', 'last_name',
                  'email', 'phone_number', 'country',
                  'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county', 'gift_aid',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'gift_aid': 'Gift Aid',
            'donation_selectors': 'Donation Selectors',
            'donation_custom': 'Donation Custom'
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'donation_custom':
                self.fields[field].widget.attrs['id'] = 'amount-custom'
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                if field != 'gift_aid':
                    self.fields[field].label = False
                else:
                    self.fields[field].label = 'Yes, I would like to Gift Aid my donation'
