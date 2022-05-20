"""Habr URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views
from mainapp.views import design, web_dev, mobile_developing, marketing, help


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='index')),
    path('design/', design, name='design'),
    path('web_dev/', web_dev, name='web_dev'),
    path('mobile_developing/', mobile_developing, name='mobile_developing'),
    path('marketing/', marketing, name='marketing'),
    path('help.html', help, name='help'),
    path('userapp/', include('userapp.urls', namespace='userapp')),
    path('comment/', include('comment.urls')),
    path('api/', include('comment.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("accounts/", include("allauth.urls")),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mainapp.views.page_not_found_view'
