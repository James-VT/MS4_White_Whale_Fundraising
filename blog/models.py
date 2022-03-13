""" Models for the blog """
from django.db import models


class Post(models.Model):
    """ Model for the posts """
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for the ordering """
        ordering = ['-date_added']


class Comment(models.Model):
    """ Model for the comments """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for the ordering """
        ordering = ['date_added']
