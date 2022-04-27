from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import *


class SectionView(ListView):
    """контроллер, отборажает Хабры с привязкой к разделам"""
    model = Habr
    allow_empty = False
    template_name = 'mainapp/habr_list.html'

    def get_queryset(self):
        return Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True)


class HabrView(DetailView):
    """контроллер, отборажает выбранный Хабр"""
    model = Habr
    allow_empty = False
    template_name = 'mainapp/habr.html'
    slug_url_kwarg = 'habr_slug'
    context_object_name = 'habr'


def index(request):
    """контроллер, возврящающий главную страницу со списком всех статей сайта"""

    habr = Habr.objects.filter(is_active = True).order_by('-time_create')
    habrs = Habr.objects.all()

    context = {
        'habr': habr,
        'habrs': habrs,
        'title': 'Главная - Проект "Хабр"',
        'index': 'selected',
        'content': 'Все потоки хабров',
    }
    return render(request, 'mainapp/index.html', context)


def design(request):
    context = {
        'title': 'Дизайн - Проект "Хабр"',
        'design': 'selected',
        'content': 'Хабры по дизайну',
    }
    return render(request, 'mainapp/index.html', context)


def web_dev(request):
    context = {
        'title': 'Веб-разработка - Проект "Хабр"',
        'web_dev': 'selected',
        'content': 'Хабры по Веб-разработке',
    }
    return render(request, 'mainapp/index.html', context)


def mobile_developing(request):
    context = {
        'title': 'Мобильная разработка - Проект "Хабр"',
        'mobile_developing': 'selected',
        'content': 'Хабры по Мобильной разработке',
    }
    return render(request, 'mainapp/index.html', context)


def marketing(request):
    context = {
        'title': 'Маркетинг - Проект "Хабр"',
        'marketing': 'selected',
        'content': 'Хабры по Маркетингу',
    }
    return render(request, 'mainapp/index.html', context)


def help(request):
    context = {
        'title': 'Помощь - Проект "Хабр"',
        'help': 'selected',
        'content': 'Краткая документация к сайту',
    }
    return render(request, 'mainapp/index.html', context)
