from urllib import request
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def preparedness(request):
    return render(request, 'preparedness.html')

def emergency_contacts(request):
    return render(request, 'emergency_contacts.html')

def calendar (request):
    return render(request, 'calendar.html')

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