""" Admin for the blog posts """
from django.contrib import admin
from .models import Post, Comment


# PostAdmin class credited to former student Jenny in readme
class PostAdmin(admin.ModelAdmin):
    """ Admin class for blog posts """
    list_display = ('title', 'slug', 'created_on', 'creator')
    prepopulated_fields = {'slug': ('title',)}


# CommentAdmin class credited to fellow student Suzy in readme
class CommentAdmin(admin.ModelAdmin):
    """ Admin class for blog post comments """
    list_display = ('body', 'created_when')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
