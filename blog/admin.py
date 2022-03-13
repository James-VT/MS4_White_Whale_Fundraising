""" Admin for the blog posts """
from django.contrib import admin

from .models import Post

admin.site.register(Post)
