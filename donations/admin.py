""" Admin for donations """
from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    """ Class for the admin of donations """
    readonly_fields = ('donation_number', 'date',
                       'donation_total', 'user_profile',)

    fields = ('donation_number', 'user_profile', 'date', 'title', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'gift_aid', 'donation_total',)

    list_display = ('donation_number', 'user_profile', 'date', 'title',
                    'first_name', 'last_name', 'gift_aid', 'donation_total',)

    ordering = ('-date',)


admin.site.register(Donation, DonationAdmin)
