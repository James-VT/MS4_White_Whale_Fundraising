""" Model for the membership choices """

from django.db import models

# Create your models here.


class MembershipLevel(models.Model):
    """Defines the level of a member's subscription"""
    GOLD = 'GO'
    SILVER = 'SI'
    BRONZE = 'BR'
    MEMBERSHIP_CHOICES = [
        (GOLD, 'Gold Level'),
        (SILVER, 'Silver Level'),
        (BRONZE, 'Bronze Level'),
    ]

    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # name = models.CharField(max_length-254)
    # friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # def __str__(self):
    #     return self.name

    # def get_friendly_name(self):
    #     return self.friendly_name
