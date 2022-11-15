from django.shortcuts import render
from django.views import generic

def reviews(request):
    return render(request, 'reviews.html')
