""" Registers the membership models for the site admin """
from django.contrib import admin
from .models import Membership

# Register your models here.


# class MembershipAdmin(admin.ModelAdmin):
#     """ Gives the admin side a proper class for memberships """
#     readonly_fields = ('membership_number', 'date', 'membership_price',
#                        'membership_level',)

#     fields = ('membership_number', 'date', 'membership_price',
#               'membership_profile', 'membership_level', 'full_name',
#               'email', 'phone_number', 'street_address1', 'street_address2',
#               'town_or_city', 'postcode', 'country',)

#     list_display = ('sku', 'level', 'description', 'price',)

#     ordering = ('sku',)


admin.site.register(Membership)
