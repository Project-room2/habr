from django.urls import path

from userapp.views import login, register, profile, logout, verify

app_name = 'userapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<int:user_id>/<hash>/', verify, name='verify'),
]
