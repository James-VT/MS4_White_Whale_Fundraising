""" Admin for user profiles """
from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    """ Class for the admin of profiles """
    readonly_fields = ('user',)

    fields = ('user', 'default_title', 'default_first_name',
              'default_last_name', 'default_email',
              'default_phone_number', 'default_country',
              'default_postcode',
              'default_town_or_city', 'default_street_address1',
              'default_street_address2',
              'default_county', 'is_member',)


admin.site.register(UserProfile, ProfileAdmin)
