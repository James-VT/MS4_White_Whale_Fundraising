""" Admin for sponsorships """
from django.contrib import admin
from .models import Sponsorship


class SponsorshipAdmin(admin.ModelAdmin):
    """ Class for the admin of sponsorships """
    readonly_fields = ('sponsorship_number', 'date',
                       'user_profile',)

    fields = ('sponsorship_number', 'user_profile', 'date', 'title', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'gift_aid',)

    list_display = ('sponsorship_number', 'date', 'title',
                    'first_name', 'last_name', 'gift_aid',)

    ordering = ('-date',)

admin.site.register(Sponsorship, SponsorshipAdmin)
