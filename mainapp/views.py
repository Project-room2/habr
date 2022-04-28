from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView

from .models import *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


def page_not_found_view(request, exception):
    return render(request, 'mainapp/404.html', status = 404)


class SectionView(ListView):
    """контроллер, отборажает хабры выбранного раздела"""

    model = Habr
    allow_empty = False
    template_name = 'mainapp/habr_list.html'

    def get_queryset(self):
        return Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True)


class HabrView(DetailView):
    """контроллер, отборажает конкретный Хабр"""

    model = Habr
    allow_empty = False
    template_name = 'mainapp/habr.html'
    slug_url_kwarg = 'habr_slug'
    context_object_name = 'habr'


def index(request):
    """контроллер, возврящающий главную страницу со списком всех статей сайта"""

    habr = Habr.objects.filter(is_active = True).order_by('-time_create')
    habrs = Habr.objects.all()
    ip = get_client_ip(request)
    #  Ip.objects.create(ip = ip)
    #  Ip.objects.get_or_create(ip)
    # if Ip.objects.filter(ip = ip).exists():
    #     Habr.views.add(Ip.objects.get(ip = ip))
    # else:
    #     Ip.objects.create(ip = ip)
    #     Habr.views.add(Ip.objects.get(ip = ip))

    context = {
        'habr': habr,
        'habrs': habrs,
        'title': 'Главная - Проект "Хабр"',
        'index': 'selected',
        'content': 'Все потоки хабров',
        'ip': ip,
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
        'help.html': 'selected',
        'content': 'Краткая документация к сайту',
    }
    return render(request, 'mainapp/help.html', context)
