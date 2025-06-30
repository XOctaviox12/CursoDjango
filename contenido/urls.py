from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.principal, name='principal'),  # Página principal
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
]