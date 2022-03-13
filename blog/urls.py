""" URLs for the blog app """
from django.urls import path
from . import views
# from blog.views import frontpage

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]