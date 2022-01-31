""" Model for the membership choices """

from django.db import models

# Create your models here.


MEMBERSHIP_CHOICES = (
    ('Gold', 'Gold Level'),
    ('Silver', 'Silver Level'),
    ('Bronze', 'Bronze Level')
)


class Membership(models.Model):
    """ Class for memberships """
    membership_level = models.CharField(
        max_length=6,
        choices=MEMBERSHIP_CHOICES,
        default='Bronze',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.membership_level


# class Membership(models.Model):
#     """ Class for memberships """
#     name = models.CharField(max_length=10)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return self.name


# class MembershipLevel(models.Model):
#     """Defines the level of a member's subscription"""
#     GOLD = 'GO'
#     SILVER = 'SI'
#     BRONZE = 'BR'
#     MEMBERSHIP_CHOICES = [
#         (GOLD, 'Gold Level'),
#         (SILVER, 'Silver Level'),
#         (BRONZE, 'Bronze Level'),
#     ]

#     level = models.CharField(max_length=6, choices=MEMBERSHIP_CHOICES,
#                              default=BRONZE,
#                              description = models.TextField(),
#                              sku = models.CharField(max_length=254,
#                              null=True, blank=True,
#                              price = models.DecimalField(max_digits=6,
#                              decimal_places=2)
#     )

#     def __str__(self):
#         return self.level in {self.GOLD, self.SILVER, self.BRONZE}

    # sku = models.CharField(max_length=254, null=True, blank=True)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=6, decimal_places=2)

    # name = models.CharField(max_length-254)
    # friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # def get_friendly_name(self):
    #     return self.friendly_name
