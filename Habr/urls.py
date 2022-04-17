"""Habr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import index, design, web_developing, mobile_developing, marketing, help

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('design/', design, name='design'),
    path('web_developing/', web_developing, name='web_developing'),
    path('mobile_developing/', mobile_developing, name='mobile_developing'),
    path('marketing/', marketing, name='marketing'),
    path('help/', help, name='help'),
]
