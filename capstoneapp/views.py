from urllib import request
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf.urls.static import static
from django.http import JsonResponse
from django.conf import settings
import requests

# INITIAL HOMEPAGE

def index(request):
    return render(request, 'index.html')


def preparedness(request):
    return render(request, 'preparedness.html')


def emergency_contacts(request):
    return render(request, 'emergency_contacts.html')


def climate(request):
    return render(request, 'weather.html',)


def earthquake(request):
    return render(request, 'earthquake.html')


def landslide(request):
    return render(request, 'landslide.html')


def reports(request):
    return render(request, 'reports.html')


def typhoon(request):
    return render(request, 'typhoon.html')


def profile(request):
    return render(request, 'profile.html')

def home_incident_reports(request):
    return render(request, 'home_incident_reports.html')

def home_incident_reports(request):
    subjects = ["Incident Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'home_incident_reports.html', context)

def home_sit_reports(request):
    return render(request, 'home_sit_reports.html')

def home_sit_reports(request):
    subjects = ["Situational Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'home_sit_reports.html', context)

def home_typhoon_reports(request):
    return render(request, 'typhoon.html')

def home_typhoon_reports(request):
    subjects = ["Typhoon Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'typhoon.html', context)

def earthquake(request):
    subjects = ["Earthquake Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'earthquake.html', context)

def landslide(request):
    subjects = ["Landslide Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'landslide.html', context)

def flood(request):
    subjects = ["Flood Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'flood.html', context)


###### BARANGAY #####
def add_report(request):
    return render(request, 'user/add_reports.html')

def incident_reports(request):
    return render(request, 'user/incident_reports.html')

@login_required(login_url='login')
def brgyhomepage(request):
    if request.user.user_type == 'barangay':
        return render(request, 'user/brgyhomepage.html')
    else:
        return HttpResponseForbidden("Access Denied")
    
def incident_reports(request):
    subjects = ["Incident Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/incident_reports.html', context)

def submit_report(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.POST)
        if serializer.is_valid():
            attachment = request.FILES.get('attachment')
            report = serializer.save(attachment=attachment)
            messages.success(request, 'Report submitted successfully.')
            return redirect('add-reports')  
        else:
            messages.error(request, 'Report submission failed. Please check your data.')
    return render(request, 'user/add-reports.html')

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


###### ADMIN ########

def admin_incident_reports(request):
    return render(request, 'admin/admin_incident_reports.html')

def admin_weather(request):
    return render(request, 'admin/admin_weather.html')

@login_required(login_url='login')
def adminhomepage(request):
    if request.user.user_type == 'mdrrmc':
        return render(request, 'admin/adminhomepage.html')
    else:
        return HttpResponseForbidden("Access Denied")

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
        return render(request, 'admin/admin_add_account.html')
    
def admin_incident_reports(request):
    subjects = ["Incident Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_incident_reports.html', context)


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




def download_attachment(request, file_name):
    report = get_object_or_404(Report, attachment__iexact=file_name)
    response = FileResponse(report.attachment)
    return response

def get_barangays(request):
    barangays = CustomUser.objects.filter(user_type='barangay').values('barangay').distinct()
    
    return JsonResponse(list(barangays), safe=False)

def get_filtered_reports(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Incident Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_sit(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Situational Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)


def get_filtered_reports_flood(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Flood Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_typhoon(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Typhoon Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_earthquake(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Earthquake Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_landslide(request):
    selected_date = request.GET.get('date')
    selected_barangay = request.GET.get('barangay')

    reports = Report.objects.filter(date_reported=selected_date, subject='Landslide Report')

    if selected_barangay:
        reports = reports.filter(barangay = selected_barangay)
    
    report_data = []
    for report in reports:
        report_data.append({
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
            'barangay': report.barangay 
        })

    return JsonResponse(report_data, safe=False)

# INITIAL HOMEPAGE

def get_weather(request):
    api_key = settings.OPENWEATHERMAP_API_KEY
    city = "Ibaan"
    country_code = "PH"
    units = "metric"
    forecast_count = 8 

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&units={units}&cnt={forecast_count}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Failed to fetch weather data."}, status=500)