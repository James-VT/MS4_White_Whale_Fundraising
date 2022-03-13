""" Forms for blog/comments """
from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Class for comment form """
    class Meta:
        """ Meta class for comment form """
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    """ Class for the post form """
    class Meta:
        """ Meta class for post form """
        model = Post
        fields = ['title', 'intro', 'body']
