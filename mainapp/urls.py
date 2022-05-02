import mainapp.views as mainapp
from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('habr/<slug:habr_slug>/', HabrView.as_view(), name = 'habr'),
    path('<slug:cat_slug>/', SectionView.as_view(), name = 'section'),
    path('like/<int:pk>/', mainapp.LikeView, name='like_post'),
]
