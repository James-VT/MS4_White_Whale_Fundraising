from django.urls import path
from .views import (
    MembershipSelectView,
)

url_patterns = [
    path('', MembershipSelectView.as_view(), name='select'),

]