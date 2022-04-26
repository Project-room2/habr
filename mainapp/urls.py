import mainapp.views as mainapp
from django.urls import path


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('habr/<slug:slug>/', mainapp.habr, name='habr'),
    path('<slug:slug>/', mainapp.section, name='section'),
    # path('changelike/<slug:slug>/', mainapp.change_like, name='change_like'),
    # path('search/', mainapp.SearchResultsView.as_view(), name='search_results'),
    # path('delete/comment/', mainapp.delete_comment, name='delete_comment'),
    # path('to/banish/', mainapp.to_banish, name='to_banish'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),m
]
