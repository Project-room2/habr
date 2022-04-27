from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path('habr/<slug:slug>/edit/', login_required(BlogUpdateView.as_view()), name='post_edit'),
    path('habr/new/', login_required(BlogCreateView.as_view()), name='post_new'),
    path('habr/<slug:slug>/', login_required(BlogDetailView.as_view()), name='post_detail'),
    path('habr/', login_required(BlogListView.as_view()), name='post_list'),
    path('habr/<slug:slug>/delete/', login_required(BlogDeleteView.as_view()), name='post_delete'),
]
