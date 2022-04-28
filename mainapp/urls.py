import mainapp.views as mainapp
from django.urls import path, re_path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp.index, name = 'index'),
    path('', IndexView.as_view(), name = 'index'),
    path('habr/<slug:habr_slug>/', HabrView.as_view(), name = 'habr'),
    path('<slug:cat_slug>/', SectionView.as_view(), name = 'section'),
    # path('changelike/<slug:slug>/', mainapp.change_like, name='change_like'),
    # path('search/', mainapp.SearchResultsView.as_view(), name='search_results'),
    # path('delete/comment/', mainapp.delete_comment, name='delete_comment'),
    # path('to/banish/', mainapp.to_banish, name='to_banish'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),m
]


