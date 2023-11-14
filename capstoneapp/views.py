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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf.urls.static import static
from django.http import JsonResponse
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
from datetime import datetime
from django.db.models import Q 
from datetime import date
from django.views.decorators.cache import cache_control
from capstoneapp.decorators import mdrrmc_required
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

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

def homeflood_basics(request):
    return render(request, 'flood_basics.html')

def hometyph_basics(request):
    return render(request, 'typhoon_basics.html')

def homeearthquake_basics(request):
    return render(request, 'earthquake_basics.html')

def homelandslide_basics(request):
    return render(request, 'landslide_basics.html')

def home_incident_reports(request):
    return render(request, 'home_incident_reports.html')

def home_mission(request):
    return render(request, 'home_mission.html')

def home_contact(request):
    return render(request, 'home_contact.html')

def home_barangays(request):
    return render(request, 'home_barangays.html')

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
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'typhoon.html', context)

def home_flood_reports(request):
    subjects = ["Flood Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

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
    reports = AdminReport.objects.filter(subject__in=subjects).order_by('-date')

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
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

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
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'flood.html', context)


###### BARANGAY #####

def userflood_basics(request):
    return render(request, 'user/userflood_basics.html')

def usertyph_basics(request):
    return render(request, 'user/usertyphoon_basics.html')

def userearthquake_basics(request):
    return render(request, 'user/userearthquake_basics.html')

def userlandslide_basics(request):
    return render(request, 'user/userlandslide_basics.html')
    

def missionvision(request):
    return render(request, 'user/user-missionvision.html')

def barangays(request):
    return render(request, 'user/user_barangay.html')

def user_contacts(request):
    return render(request, 'user/user_contacts.html')

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


def user_flood(request):
    subjects = ["Flood Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/user_flood.html', context)

def user_typhoon(request):
    subjects = ["Typhoon Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/user_typhoon.html', context)

def user_earthquake(request):
    subjects = ["Earthquake Report"]
    reports = AdminReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/user_earthquake.html', context)

def user_landslide(request):
    subjects = ["Landslide Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/user_landslide.html', context)

def user_sit(request):
    subjects = ["Situational Report"]
    reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'user/user_sit.html', context)

def get_userreports(request):
    return render(request, 'user/user_allreports.html')
@api_view(['GET'])
def user_allreports(request):
        date_param = request.GET.get('date', None)
        subject_param = request.GET.get('subject', None)

        page = request.GET.get('page', 1)

        logged_in_barangay = request.user.barangay 
        reports = Report.objects.filter(barangay=logged_in_barangay)

        if date_param:
            try:
                selected_date = datetime.strptime(date_param, '%Y-%m-%d').date()
                reports = reports.filter(date_reported=selected_date)
            except ValueError:
                return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        if subject_param:
            reports = reports.filter(subject__icontains=subject_param)

        reports = reports.order_by('-date_reported', '-time_reported')

        items_per_page = 10

        paginator = Paginator(reports, items_per_page)

        try:
            page_reports = paginator.page(page)
        except EmptyPage:
            return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReportSerializer(page_reports, many=True)

        pagination_data = {
            'total_pages': paginator.num_pages,
            'has_next': page_reports.has_next(),
            'has_previous': page_reports.has_previous(),
        }

        return Response({
            "reports": serializer.data,
            "pagination": pagination_data,
        })

@api_view(['PUT'])
def edit_report(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(report, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_subjects(request):
    subjects = Report.SUBJECT_CHOICES
    return Response(subjects)

@api_view(['DELETE'])
def delete_report(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Report.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
    
def user_weather(request):
    return render(request, 'user/user_weather.html')

def submit_report(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.POST)
        if serializer.is_valid():
            attachment = request.FILES.get('attachment')
            report = serializer.save(attachment=attachment)
            messages.success(request, 'Report submitted successfully.')

            subject = 'New Report Submitted'
            message = 'A new report has been submitted by a barangay user.'
            from_email = 'mdrrmcibaanreports@gmail.com'
            recipient_list = ['mdrrmcibaan@gmail.com']

            html_content = get_template('report_notification.html').render({'report': report})

            email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
            email.attach_alternative(html_content, "text/html")

            email.send()

            return redirect('add-reports')  
        else:
            messages.error(request, 'Report submission failed. Please check your data.')
    return render(request, 'user/add_reports.html')

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

def get_user_announcements(request):
    if request.user.user_type == 'barangay':
        try:
            announcements = Announcement.objects.filter(barangay=request.user).order_by('-date')
        except ValueError:
            return HttpResponse("Invalid barangay object or relationship")

        selected_date = request.GET.get('date')
        selected_subject = request.GET.get('subject')

        if selected_date:
            try:
                selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
                announcements = announcements.filter(date=selected_date)
            except ValueError:
                return HttpResponse("Invalid date format")

        if selected_subject:
            announcements = announcements.filter(Q(subject__icontains=selected_subject))

        items_per_page = 10
        paginator = Paginator(announcements, items_per_page)

        page_number = request.GET.get('page')
        try:
            announcements = paginator.page(page_number)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator.num_pages)

        total_barangays_count = CustomUser.objects.filter(user_type='barangay').count()

        context = {
            'announcements': announcements,
            'total_barangays_count': total_barangays_count,

        }
        print(context)

        return render(request, 'user/user-announcements.html', context)
    else:
        return HttpResponseForbidden("Access Denied")

###### ADMIN ########

def adminflood_basics(request):
    return render(request, 'admin/adminflood_basics.html')

def admintyph_basics(request):
    return render(request, 'admin/admintyphoon_basics.html')

def adminearthquake_basics(request):
    return render(request, 'admin/adminearthquake_basics.html')

def adminlandslide_basics(request):
    return render(request, 'admin/adminlandslide_basics.html')
    

def add_earthquakereport(request):
    return render(request, 'admin/add_earthquakereport.html')

def admin_mission(request):
    return render(request, 'admin/admin_missionvision.html')

def admin_barangays(request):
    return render(request, 'admin/admin_barangays.html')

def admin_contact(request):
    return render(request, 'admin/admin_contact.html')

@mdrrmc_required
def admin_incident_reports(request):
    return render(request, 'admin/admin_incident_reports.html')

@mdrrmc_required
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
                
            print(request.data)

            return redirect('register')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return render(request, 'admin/admin_add_account.html')

@mdrrmc_required
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

@cache_control(no_store=True, must_revalidate=True)
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
@mdrrmc_required
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

@mdrrmc_required
def admin_typhoon_reports(request):
    subjects = ["Typhoon Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_typhoon_reports.html', context)

# def admin_earthquake_reports(request):
#     subjects = ["Earthquake Report"]
#     reports = Report.objects.filter(subject__in=subjects).order_by('-date_reported')

#     reports_per_page = 10
#     paginator = Paginator(reports, reports_per_page)

#     page = request.GET.get('page')
#     reports = paginator.get_page(page)

#     context = {
#         'reports': reports
#     }

#     return render(request, 'admin/admin_earthquake_reports.html', context)
@mdrrmc_required

def admin_earthquake_reports(request):
    admin_reports_list = AdminReport.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(admin_reports_list, 10)

    try:
        admin_reports = paginator.page(page)
    except PageNotAnInteger:
        admin_reports = paginator.page(1)
    except EmptyPage:
        admin_reports = paginator.page(paginator.num_pages)

    return render(request, 'admin/admin_earthquake_reports.html', {'reports': admin_reports})

@mdrrmc_required
def admin_landslide_reports(request):
    subjects = ["Landslide Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }

    return render(request, 'admin/admin_landslide_reports.html', context)

@mdrrmc_required
def admin_flood_reports(request):
    subjects = ["Flood Report"]
    reports = AdminNaturalReport.objects.filter(subject__in=subjects).order_by('-date_reported')

    reports_per_page = 10
    paginator = Paginator(reports, reports_per_page)

    page = request.GET.get('page')
    reports = paginator.get_page(page)

    context = {
        'reports': reports
    }
    return render(request, 'admin/admin_flood_reports.html', context)

@mdrrmc_required
def add_announcement(request):
    return render(request, 'admin/add-announcement.html')

@mdrrmc_required
def submit_announcement(request):
    if request.method == 'POST':
        serializer = AnnouncementSerializer(data=request.POST)
        print(request.POST)
        if serializer.is_valid():
            announcement = serializer.save()
            
            if 'all' in request.POST:
                all_barangays = CustomUser.objects.filter(user_type='barangay')
                announcement.barangay.set(all_barangays)
            else:
                selected_barangay_ids = request.POST.getlist('barangay')
                selected_barangays = CustomUser.objects.filter(pk__in=selected_barangay_ids, user_type='barangay')
            
            announcement.barangay.set(selected_barangays)
            messages.success(request, 'Announcement submitted successfully.')
            return redirect('add_announcement')
        else:
            messages.error(request, 'Announcement submission failed. Please check your data.')
            return render(request, 'admin/add-announcement.html', {'form': serializer})
    else:
        form = AnnouncementSerializer()
        return render(request, 'admin/add-announcement.html', {'form': form})

@mdrrmc_required
def get_announcement(request):
    return render(request, 'admin/admin-announcement.html')

@mdrrmc_required
def get_announcements(request):
    announcements = Announcement.objects.all().order_by('-date')

    selected_date = request.GET.get('date')
    selected_subject = request.GET.get('subject')

    if selected_date:
        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
            announcements = Announcement.objects.filter(date=selected_date)
        except ValueError:
            return JsonResponse({"error": "Invalid date format"}, status=400)
    else:
        announcements = Announcement.objects.all().order_by('-date')
    
    if selected_subject:
        announcements = announcements.filter(Q(subject__icontains=selected_subject))


    items_per_page = 10
    paginator = Paginator(announcements, items_per_page)

    page_number = request.GET.get('page')
    try:
        announcements = paginator.page(page_number)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)

    total_pages = paginator.num_pages
    data = []

    for announcement in announcements:
        barangays = announcement.barangay.all()
        barangay_names = [barangay.barangay for barangay in barangays]

        announcement_data = {
            "id": announcement.id,
            "subject": announcement.subject,
            "description": announcement.description,
            "date": announcement.date.strftime('%Y-%m-%d'), 
            "barangays": barangay_names,
        }

        data.append(announcement_data)

    pagination_info = {
        "total_pages": paginator.num_pages,
        "has_previous": announcements.has_previous(),
        "has_next": announcements.has_next(),
        "previous_page_number": announcements.previous_page_number() if announcements.has_previous() else None,
        "next_page_number": announcements.next_page_number() if announcements.has_next() else None,
    }

    response_data = {
        "announcements": data,
        "pagination_info": pagination_info,
    }

    return JsonResponse(response_data, safe=False)

@mdrrmc_required
def get_reports(request):
    return render(request, 'admin/admin_all_reports.html')

@mdrrmc_required
def new_reports(request):
    return render(request, 'admin/new_reports.html')

@mdrrmc_required
@api_view(['GET'])
def get_reports_for_today(request):
    today = date.today()
    subject_query = request.GET.get('subject')
    page = request.GET.get('page', 1)

    today_reports = Report.objects.filter(date_reported=today)
    
    if subject_query:
        today_reports = today_reports.filter(subject__icontains=subject_query)

    today_reports = today_reports.order_by('-date_reported', '-time_reported')

    items_per_page = 10  

    paginator = Paginator(today_reports, items_per_page)

    try:
        page_reports = paginator.page(page)
    except EmptyPage:
        return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(page_reports, many=True)

    pagination_data = {
        'total_pages': paginator.num_pages,
        'has_next': page_reports.has_next(),
        'has_previous': page_reports.has_previous(),
        'next_page_number': page_reports.next_page_number() if page_reports.has_next() else None,
        'previous_page_number': page_reports.previous_page_number() if page_reports.has_previous() else None,
    }

    return Response({
        "reports": serializer.data,
        "pagination": pagination_data,
    })

@mdrrmc_required
@api_view(['GET'])
def get_all_reports(request):
    date_param = request.GET.get('date', None)
    subject_param = request.GET.get('subject', None)

    page = request.GET.get('page', 1)

    reports = Report.objects.all()

    if date_param:
        try:
            selected_date = datetime.strptime(date_param, '%Y-%m-%d').date()
            reports = reports.filter(date_reported=selected_date)
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

    if subject_param:
        reports = reports.filter(subject__icontains=subject_param)

    reports = reports.order_by('-date_reported', '-time_reported')

    items_per_page = 10

    paginator = Paginator(reports, items_per_page)

    try:
        page_reports = paginator.page(page)
    except EmptyPage:
        return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(page_reports, many=True)

    pagination_data = {
        'total_pages': paginator.num_pages,
        'has_next': page_reports.has_next(),
        'has_previous': page_reports.has_previous(),
    }

    return Response({
        "reports": serializer.data,
        "pagination": pagination_data,
    })

def get_report_details(request):
    report_id = request.GET.get('report_id')

    if not report_id:
        return JsonResponse({"error": "Report ID is required"}, status=400)

    try:
        report = Report.objects.get(id=report_id)
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data)
    except Report.DoesNotExist:
        raise Http404("Report not found")

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_update(self, serializer):
        formatted_date = self.request.data.get('date')

        date_object = datetime.strptime(formatted_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        serializer.save(date=date_object)

@mdrrmc_required
def view_barangay(request):
    return render(request, 'admin/view_barangay.html')

def download_attachment(request, file_name):
    report = get_object_or_404(Report, attachment__iexact=file_name)
    response = FileResponse(report.attachment)
    return response

def get_barangays(request):
    barangays = CustomUser.objects.filter(user_type='barangay').values('barangay', 'id').distinct()
    return JsonResponse(list(barangays), safe=False)
@mdrrmc_required
def list_of_admin(request):
    barangays = CustomUser.objects.filter(user_type='mdrrmc').values('id','barangay', 'email', 'contact_number').distinct()
    
    context = {
        'barangays': barangays,
    }

    return render(request, 'admin/view_admin.html', context)
@mdrrmc_required
def list_of_barangays(request):
    barangays = CustomUser.objects.filter(user_type='barangay').values('id','barangay', 'email', 'contact_number').distinct()
    
    context = {
        'barangays': barangays,
    }

    return render(request, 'admin/view_barangay.html', context)
@mdrrmc_required
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
@mdrrmc_required
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

    reports = AdminNaturalReport.objects.filter(date_reported=selected_date, subject='Flood Report')
    
    report_data = []
    for report in reports:
        report_data.append({
            'id': report.id,
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_typhoon(request):
    selected_date = request.GET.get('date')

    reports = AdminNaturalReport.objects.filter(date_reported=selected_date, subject='Typhoon Report')
    
    report_data = []
    for report in reports:
        report_data.append({
            'id': report.id,
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_earthquake(request):
    selected_date = request.GET.get('date')
    reports = AdminReport.objects.filter(date=selected_date, subject='Earthquake Report')

    
    report_data = []
    for report in reports:
        report_data.append({
            'id': report.id,
            'subject': report.subject,
            'description': report.description,
            'date': report.date.strftime('%Y-%m-%d'),
            'time': report.time.strftime('%H:%M'),
        })

    return JsonResponse(report_data, safe=False)

def get_filtered_reports_landslide(request):
    selected_date = request.GET.get('date')

    reports = AdminNaturalReport.objects.filter(date_reported=selected_date, subject='Landslide Report')
    
    report_data = []
    for report in reports:
        report_data.append({
            'id': report.id,
            'subject': report.subject,
            'description': report.description,
            'attachment': report.attachment.url if report.attachment else '',
            'date_reported': report.date_reported.strftime('%Y-%m-%d'),
            'time_reported': report.time_reported.strftime('%H:%M'),
        })

    return JsonResponse(report_data, safe=False)

from django.shortcuts import render

@api_view(['POST'])
def admin_submit_report(request):
    subject = request.data.get('subject')
    description = request.data.get('description')

    if subject == 'Earthquake Report':
        serializer = AdminReportSerializer(data=request.data)
    else:
        serializer = AdminNaturalReportSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        messages.success(request, 'Report submitted successfully.')  
        return render(request, 'admin/add_earthquakereport.html')
    
    messages.error(request, 'Error submitting report. Please check the form.')
    return render(request, 'admin/add_earthquakereport.html', {'serializer': serializer})  

@api_view(['PUT'])
def edit_admin_report(request, report_id):
    try:
        report = AdminNaturalReport.objects.get(pk=report_id)
    except AdminNaturalReport.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AdminNaturalReportSerializer(report, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_admin_subjects(request):
    subjects = AdminNaturalReport.SUBJECT_CHOICES
    return Response(subjects)

@api_view(['DELETE'])
def delete_admin_report(request, report_id):
    try:
        report = AdminNaturalReport.objects.get(pk=report_id)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except AdminNaturalReport.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

def get_admin_report_details(request):
    report_id = request.GET.get('report_id')

    if not report_id:
        return JsonResponse({"error": "Report ID is required"}, status=400)

    try:
        report = AdminNaturalReport.objects.get(id=report_id)
        serializer = AdminNaturalReportSerializer(report)
        return JsonResponse(serializer.data)
    except AdminNaturalReport.DoesNotExist:
        raise Http404("Report not found")
    
def get_earthquake_admin_report_details(request):
    report_id = request.GET.get('report_id')

    if not report_id:
        return JsonResponse({"error": "Report ID is required"}, status=400)

    try:
        report = AdminReport.objects.get(id=report_id)
        serializer = AdminReportSerializer(report)
        return JsonResponse(serializer.data)
    except AdminReport.DoesNotExist:
        raise Http404("Report not found")

@api_view(['PUT'])
def edit_earthquake_report(request, report_id):
    try:
        report = AdminReport.objects.get(pk=report_id)
    except AdminReport.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AdminReportSerializer(report, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_earthquake_report(request, report_id):
    try:
        report = AdminReport.objects.get(pk=report_id)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except AdminReport.DoesNotExist:
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
    
def add_adminreport(request):
    return render(request, 'admin/add_earthquakereport.html')

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