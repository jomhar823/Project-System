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
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets

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

            return redirect('register')
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


# def admin_sit_reports(request):
#     return render(request, 'admin_sit_reports.html')

def admin_sit_reports(request):
    subjects = ["Situational Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_sit_reports.html', context)


def admin_typhoon_reports(request):
    subjects = ["Typhoon Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_typhoon_reports.html', context)

def admin_earthquake_reports(request):
    subjects = ["Earthquake Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_earthquake_reports.html', context)

def admin_landslide_reports(request):
    subjects = ["Landslide Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_landslide_reports.html', context)

def admin_flood_reports(request):
    subjects = ["Flood Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_flood_reports.html', context)

def add_announcement(request):
    return render(request, 'admin/add-announcement.html')

def submit_announcement(request):
    if request.method == 'POST':
        serializer = AnnouncementSerializer(data=request.POST)
        if serializer.is_valid():
            print("Form is valid. Submitting announcement.")
            announcement = serializer.save()
            
            selected_barangay_ids = request.POST.getlist('barangay')
            selected_barangays = CustomUser.objects.filter(pk__in=selected_barangay_ids, user_type='barangay')
            
            announcement.barangay.set(selected_barangays)
            messages.success(request, 'Announcement submitted successfully.')
            return redirect('add_announcement')
        else:
            print("Form is not valid. Errors:", serializer.errors)
            messages.error(request, 'Announcement submission failed. Please check your data.')
            return render(request, 'admin/add-announcement.html', {'form': serializer})
    else:
        form = AnnouncementSerializer()
        return render(request, 'admin/add-announcement.html', {'form': form})

def get_announcement(request):
    return render(request, 'admin/admin-announcement.html')

def get_announcements(request):
    announcements = Announcement.objects.all()
    data = [{"id": announcement.id,"subject": announcement.subject, "description": announcement.description, "date": announcement.date} for announcement in announcements]
    return JsonResponse(data, safe=False)

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


def view_barangay(request):
    return render(request, 'admin/view_barangay.html')

def download_attachment(request, file_name):
    report = get_object_or_404(Report, attachment__iexact=file_name)
    response = FileResponse(report.attachment)
    return response

def get_barangays(request):
    barangays = CustomUser.objects.filter(user_type='barangay').values('barangay', 'id').distinct()
    return JsonResponse(list(barangays), safe=False)

def list_of_admin(request):
    barangays = CustomUser.objects.filter(user_type='mdrrmc').values('id','barangay', 'email', 'contact_number').distinct()
    
    context = {
        'barangays': barangays,
    }

    return render(request, 'admin/view_admin.html', context)

def list_of_barangays(request):
    barangays = CustomUser.objects.filter(user_type='barangay').values('id','barangay', 'email', 'contact_number').distinct()
    
    context = {
        'barangays': barangays,
    }

    return render(request, 'admin/view_barangay.html', context)

@csrf_exempt
def update_barangay(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)  
            barangay_id = data['id']
            new_barangay_name = data['barangay']
            new_email = data['email']
            new_contact_number = data['contact_number']

            barangay = CustomUser.objects.get(id=barangay_id)
            barangay.barangay = new_barangay_name
            barangay.email = new_email
            barangay.contact_number = new_contact_number
            barangay.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
@csrf_exempt
def delete_barangay(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            barangay_id = data.get('id')
            
            if barangay_id:
                barangay = CustomUser.objects.get(id=barangay_id)
                barangay.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Barangay ID is missing from the request.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})




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