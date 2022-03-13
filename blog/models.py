""" Models for the blog """
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    """ Model for the posts """
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    updated_when = models.DateTimeField(auto_now_add=True)
    intro = models.TextField()
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="post")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for the ordering """
        ordering = ['-created_on']

    def __str__(self):
        return self.title


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    """ Function to generate a slug if one does not exist """
    if not instance.slug:
        instance.slug = slugify(
            instance.creator.username + "-" + instance.title
        )


pre_save.connect(pre_save_blog_post_receiver, sender=Post)


class Comment(models.Model):
    """ Model for the comments """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name="comment", default=1)
    body = models.TextField()
    created_when = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for the ordering """
        ordering = ['-created_when']
