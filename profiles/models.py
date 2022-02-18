""" Models for members' profiles """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for storing default contact info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates the user profile
    """
    # if created:
    UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.userprofile.save()
