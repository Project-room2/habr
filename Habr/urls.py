"""Habr URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import index, design, web_developing, mobile_developing, marketing, help


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    # path('', index, name='index'),
    path('design/', design, name='design'),
    path('web_developing/', web_developing, name='web_developing'),
    path('mobile_developing/', mobile_developing, name='mobile_developing'),
    path('marketing/', marketing, name='marketing'),
    path('help/', help, name='help'),
    path('userapp/', include('userapp.urls', namespace='userapp')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
