
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index', views.index, name='mainpage'),
    path('login', views.login_view, name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('adminhomepage', views.adminhomepage, name='adminhomepage'),
    path('brgyhomepage', views.brgyhomepage, name='brgyhomepage'),
    path('', views.index, name='index'),
    path('preparedness', views.preparedness, name='preparedness'),
    path('emergency_contacts', views.emergency_contacts, name='emergency_contacts'),
    path('weather', views.climate, name="weather"),
    path('earthquake', views.earthquake, name="earthquake"),
    path('landslide', views.landslide, name="landslide"),
    path('reports', views.reports, name="reports"),
    path('add-reports', views.add_report, name='add-reports'),
    path('incident-reports', views.incident_reports, name='incident-reports'),
    path('get_user_announcements', views.get_user_announcements, name='get_user_announcements'),


    path('admin_incident_reports', views.admin_incident_reports, name='admin_incident_reports'),
    path('admin_weather', views.admin_weather, name='admin_weather'),
    path('admin_sit_reports', views.admin_sit_reports, name='admin_sit_reports'),
    path('admin_typhoon_reports', views.admin_typhoon_reports, name='admin_typhoon_reports'),
    path('admin_earthquake_reports', views.admin_earthquake_reports, name='admin_earthquake_reports'),
    path('admin_landslide_reports', views.admin_landslide_reports, name='admin_landslide_reports'),
    path('admin_flood_reports', views.admin_flood_reports, name='admin_flood_reports'),
    path('view_barangay', views.view_barangay, name="view_barangay"),
    path('list-of-barangays', views.list_of_barangays, name='list_of_barangays'),
    path('update-barangay/', views.update_barangay, name='update_barangay'),
    path('delete_barangay/', views.delete_barangay, name='delete_barangay'),
    path('add_announcement', views.add_announcement, name='add_announcement'),
    path('get_announcement', views.get_announcement, name='get_announcement'),
    path('get_announcements', views.get_announcements, name='get_announcements'),
    path('get_reports', views.get_reports, name='get_reports'),
    path('get_reports_for_today', views.get_reports_for_today, name='get_reports_for_today'),
    path('get_all_reports', views.get_all_reports, name='get_all_reports'),
    path('get_report_details', views.get_report_details, name='get_report_details'),
    path('new_reports', views.new_reports, name='new_reports'),


    path('submit_announcement/', views.submit_announcement, name='submit_announcement'),
    path('announcement/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement-detail'),




    path('home_incident_reports', views.home_incident_reports, name='home_incident_reports'),
    path('home_sit_reports', views.home_sit_reports, name='home_sit_reports'),
    path('home_typhoon_reports', views.home_typhoon_reports, name='home_typhoon_reports'),
    path('home_typhoon_reports', views.home_typhoon_reports, name='home_typhoon_reports'),
    path('flood', views.flood, name="flood"),


    path('download-attachment/<str:file_name>/', views.download_attachment, name='download_attachment'),
    path('get_barangays/', views.get_barangays, name='get_barangays'),
    path('get_filtered_reports/', views.get_filtered_reports, name='get_filtered_reports'),
    path('get_filtered_reports_sit/', views.get_filtered_reports_sit, name='get_filtered_reports_sit'),
    path('get_filtered_reports_flood/', views.get_filtered_reports_flood, name='get_filtered_reports_flood'),
    path('get_filtered_reports_typhoon/', views.get_filtered_reports_typhoon, name='get_filtered_reports_typhoon'),

    path('get_filtered_reports_earthquake/', views.get_filtered_reports_earthquake, name='get_filtered_reports_earthquake'),
    path('get_filtered_reports_landslide/', views.get_filtered_reports_landslide, name='get_filtered_reports_landslide'),


    #climate
    path('get-weather/', views.get_weather, name='get-weather'),


    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),

    # MANAGE REPORT
    path('submit-report/', views.submit_report, name='submit_report'),
    path('reports/<int:pk>/', views.ReportDetailView.as_view(), name='report-detail'),
    path('view-incident-reports/', views.incident_reports, name='view-incident-reports'),

    #
    path('view-admin-incident-reports/', views.admin_incident_reports, name='view-admin-incident-reports'),


]
