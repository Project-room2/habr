from django.urls import path, include

from .views import habr_create

app_name = 'habrapp'

urlpatterns = [
    path('create/', habr_create, name='create'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
