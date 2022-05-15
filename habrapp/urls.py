from django.urls import path

from .views import habr_create

app_name = 'habrapp'

urlpatterns = [
             path('create/', habr_create, name='create'),
]