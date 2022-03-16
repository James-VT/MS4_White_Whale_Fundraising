""" Tells Django where things are stored """
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Tells Django where things are stored """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Tells Django where things are stored """
    location = settings.MEDIAFILES_LOCATION
