""" Models for the donation form """
import uuid
from django.db import models
from django_countries.fields import CountryField


class Donation(models.Model):
    """ Class for handling donations """
    donation_number = models.CharField(max_length=32,
                                       null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    donation_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         null=False, default=0)

    def _generate_donation_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # def update_total(self):
    #     """
    #     Update the donation amount according to a user's input
    #     """
    #     self.donation_total = self.


# class DonationValue(models.Model):
#     """ Class for obtaining the donation value """
#     donation_value = models.DecimalField(max_digits=6, decimal_places=2,
#                                          null=False, blank=False,
#                                          editable=False)