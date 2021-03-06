""" Models for the donation form """
import uuid
from django.db import models
from django import forms
from django_countries.fields import CountryField

from django.conf import settings

from profiles.models import UserProfile


class Donation(models.Model):
    """ Class for handling donations """

    donation_number = models.CharField(max_length=32,
                                       null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='donations')
    title = models.CharField(max_length=32, null=False, blank=False,
                             default="")
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False,
                                 default="")
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    gift_aid = models.BooleanField(default=False)
    donation_total = models.DecimalField(max_digits=6, default=0,
                                         decimal_places=2,
                                         null=False, blank=False)

    def _generate_donation_number(self):
        """
        Generate a random, unique donation number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the donation number
        if it hasn't been set already - nice failsafe
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donation_number
