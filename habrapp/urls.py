from django.urls import path, include
from .views import habr_create, HabrListView, habr_restore, habr_publish, habr_remove, HabrEdit

app_name = 'habrapp'

urlpatterns = [
    path('create/', habr_create, name='create'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('myhabrlist/', HabrListView.as_view(), name='myhabrlist'),
    path('publish/<slug:habr_slug>/', habr_publish, name='publish'),
    path('remove/<slug:habr_slug>/', habr_remove, name='remove'),
    path('restore/<slug:habr_slug>/', habr_restore, name='restore'),
    path('edit/<slug:habr_slug>/', HabrEdit.as_view(), name='edit'),
]
