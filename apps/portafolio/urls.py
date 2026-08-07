from django.contrib import admin
from django.urls import path
from apps.portafolio.views import HomeView

app_name = 'portafolio'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
]
