from urllib import request
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

def profile(request):
    # Your view logic here
    return render(request, 'profile.html')

@login_required
def home(request):
    return render(request, 'home.html')


def preparedness(request):
    return render(request, 'preparedness.html')


def emergency_contacts(request):
    return render(request, 'emergency_contacts.html')


def climate(request):
    return render(request, 'climate.html',)


def earthquake(request):
    return render(request, 'earthquake.html')


def landslide(request):
    return render(request, 'landslide.html')


def reports(request):
    return render(request, 'reports.html')


def typhoon(request):
    return render(request, 'typhoon.html')


def weathersit(request):
    return render(request, 'weathersit.html')
