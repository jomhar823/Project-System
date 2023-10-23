
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
    path('climate', views.climate, name="climate"),
    path('earthquake', views.earthquake, name="earthquake"),
    path('landslide', views.landslide, name="landslide"),
    path('typhoon', views.typhoon, name="typhoon"),
    path('reports', views.reports, name="reports"),
    path('weather_situation', views.weathersit, name="weathersit"),
    path('home', views.home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name='logout'),

]
