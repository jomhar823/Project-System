from urllib import request
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')
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

def profile(request):
    return render(request, 'profile.html')

def adminhomepage(request):
    return render(request, 'adminhomepage.html')

def brgyhomepage(request):
    return render(request, 'brgyhomepage.html')

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            user_type = request.data.get('user_type')
            if user_type == 'mdrrmc':
                user.is_superuser = True
                user.is_staff = True
                user.save()

            return redirect('mainpage')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return render(request, 'admin_add_account.html')


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password=password)

        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == 'mdrrmc':
                return redirect('adminhomepage')
            elif user_type == 'barangay':
                return redirect('brgyhomepage')
        else:
            print("Authentication failed")

    return render(request, 'login.html')