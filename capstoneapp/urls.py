
from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.login, name="login"),
    path('', views.home, name="home"),
    path('preparedness', views.preparedness, name='preparedness'),
    path('emergency_contacts', views.emergency_contacts, name='emergency_contacts'),
    path('climate', views.climate, name="climate"),
    path('earthquake', views.earthquake, name="earthquake"),
    path('landslide', views.landslide, name="landslide"),
    path('typhoon', views.typhoon, name="typhoon"),
    path('reports', views.reports, name="reports"),
    path('weather_situation', views.weathersit, name="weathersit"),
]
