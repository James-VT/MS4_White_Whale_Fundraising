""" Model for the sponsorship """
import uuid
from django.db import models
from django import forms
from django_countries.fields import CountryField
from profiles.models import UserProfile


class Sponsorship(models.Model):
    """ Class for sponsorship model """
    started_on = models.DateField(auto_now_add=True)
    sponsorship_number = models.CharField(max_length=32,
                                       null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='sponsorship')
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


    def _generate_sponsorship_number(self):
        """
        Generate a random, unique sponsorship number using UUID
        """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the sponsorship number
        if it hasn't been set already - nice failsafe
        """
        if not self.sponsorship_number:
            self.sponsorship_number = self._generate_sponsorship_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sponsorship_number
