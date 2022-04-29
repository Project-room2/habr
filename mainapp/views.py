from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
    """контроллер, отборажает активные и разрешенные к публикации Хабры выбранного раздела"""

    model = Habr
    paginate_by = 2
    allow_empty = True
    template_name = 'mainapp/habr_list.html'
    context_object_name = 'habr'

    def get_queryset(self):
        return Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True, is_active = True)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['habr'][0].category) + ' - Xabr '
        context['cat_selected'] = context['habr'][0].category.id
        return context


class HabrView(DetailView):
    """контроллер, отборажает конкретный Хабр"""

    model = Habr
    allow_empty = True
    template_name = 'mainapp/habr.html'
    slug_url_kwarg = 'habr_slug'
    context_object_name = 'habr'

    def get_queryset(self):
        return Habr.objects.filter(is_published = True, is_active = True)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Xabr - ' + str(context['habr'])
        context['cat_selected'] = '0'

        # =
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return context


class IndexView(ListView):
    """контроллер, отборажает все активныее и разрешениые к публикации Хабры на главной """

    paginate_by = 2
    model = Habr
    allow_empty = True
    template_name = 'mainapp/index.html'
    context_object_name = 'habrs'

    def get_queryset(self):
        return Habr.objects.filter(is_published = True, is_active = True)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Xabr - знания это сила!'
        context['cat_selected'] = '0'
        return context


def design(request):
    context = {
        'title': 'Дизайн - Xabr"',
        'design': 'selected',
        'content': 'Хабры по дизайну',
    }
    return render(request, 'mainapp/index.html', context = context)


def web_dev(request):
    context = {
        'title': 'Веб-разработка - Xabr"',
        'web_dev': 'selected',
        'content': 'Хабры по Веб-разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def mobile_developing(request):
    context = {
        'title': 'Мобильная разработка - Xabr',
        'mobile_developing': 'selected',
        'content': 'Хабры по Мобильной разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def marketing(request):
    context = {
        'title': 'Маркетинг - Xabr',
        'marketing': 'selected',
        'content': 'Хабры по Маркетингу',
    }
    return render(request, 'mainapp/index.html', context = context)


def help(request):
    context = {
        'title': 'Помощь - Xabr',
        'content': 'Краткая документация к сайту',
        'cat_selected': 5
    }
    return render(request, 'mainapp/help.html', context = context)

def Like(request, slug):
    post = get_object_or_404(Habr, id=request.POST.get('like_slug'))
    print(post)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('like', args=[str(like_slug)]))
