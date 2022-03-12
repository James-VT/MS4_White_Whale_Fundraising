""" Model for the membership choices """

from django.db import models

# Create your models here.


class Membership(models.Model):
    """ Class for memberships """
    name = models.CharField(max_length=10, default='')
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
