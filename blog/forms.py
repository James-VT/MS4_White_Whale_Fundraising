""" Forms for blog/comments """
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """ Class for comment form """
    class Meta:
        """ Meta class for comment form """
        model = Comment
        fields = ['name', 'email', 'body']