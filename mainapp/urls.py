from django.template.defaulttags import url
import mainapp.views as mainapp
from django.urls import path, re_path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp.index, name = 'index'),
    path('', IndexView.as_view(), name = 'index'),
    path('habr/<slug:habr_slug>/', HabrView.as_view(), name = 'habr'),
    path('<slug:cat_slug>/', SectionView.as_view(), name = 'section'),
    path('like/<int:pk>/', mainapp.LikeView, name='like_post'),
]
