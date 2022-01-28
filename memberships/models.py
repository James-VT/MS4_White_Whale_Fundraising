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

    # name = models.CharField(max_length-254)
    # friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # def __str__(self):
    #     return self.name

    # def get_friendly_name(self):
    #     return self.friendly_name
