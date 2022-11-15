import django as django
from django.urls import path
from .views import *

urlpatterns = [
    path('reviews', reviews, name='reviews'),

]




