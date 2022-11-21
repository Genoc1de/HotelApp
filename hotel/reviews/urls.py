import django as django
from django.urls import path
from .views import *

urlpatterns = [
    path('reviews', post_detail, name='post_detail'),

]




