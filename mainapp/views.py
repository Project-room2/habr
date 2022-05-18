from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


def page_not_found_view(request, exception):
    return render(request, 'mainapp/404.html', {'path': request.path}, status = 404)


class SectionView(ListView):
    """ Контроллер, отборажает активные и разрешенные к публикации Хабры выбранного раздела """

    model = Habr
    paginate_by = 2
    allow_empty = True
    template_name = 'mainapp/habr_list.html'
    context_object_name = 'habr'

    def get_queryset(self):
        return Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True, is_active = True)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(context['habr']) > 0:
            context['title'] = str(context['habr'][0].category) + ' - Xabr '
            context['cat_selected'] = context['habr'][0].category.id
        else:
            context['title'] = 'Ищем автора для этого раздела!'
            context['cat_selected'] = ''
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

        # Счетчик кол-во открытия хабров
        object = self.get_object()
        object.habr_view += 1
        object.save()

        # Считаем лайки
        stuff = get_object_or_404(Habr, slug = self.kwargs['habr_slug'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        context['us'] = 5

        return context


class IndexView(ListView):
    """ Контроллер, отображает все активныее и разрешениые к публикации Хабры на главной """

    paginate_by = 4
    model = Habr
    allow_empty = True
    template_name = 'mainapp/index.html'
    context_object_name = 'habrs'

    def get_queryset(self):
        return Habr.objects.filter(is_published = True, is_active = True)

    def get_context_data(self, *, object_list = None, **kwargs):

        context = super().get_context_data()
        context['title'] = 'Xabr - знания это сила!'
        context['cat_selected'] = 0
        context['art'] = Habr.objects.filter(is_published = True, is_active = True).order_by('-habr_view')
        context['author'] = Habr.objects.order_by().values('user').distinct()
        return context


def design(request):
    """ Функция рендерит раздел "Дизайн", включая SEO-разметку """

    context = {
        'title': 'Дизайн - Xabr"',
        'design': 'selected',
        'content': 'Хабры по дизайну',
    }
    return render(request, 'mainapp/index.html', context = context)


def web_dev(request):
    """ Функция рендерит раздел "Веб-разработку", включая SEO-разметку """

    context = {
        'title': 'Веб-разработка - Xabr"',
        'web_dev': 'selected',
        'content': 'Хабры по Веб-разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def mobile_developing(request):
    """ Функция рендерит раздел "Мобильная разработка", включая SEO-разметку """

    context = {
        'title': 'Мобильная разработка - Xabr',
        'mobile_developing': 'selected',
        'content': 'Хабры по Мобильной разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def marketing(request):
    """ Функция рендерит раздел "Маркетинг", включая SEO-разметку """

    context = {
        'title': 'Дизайн - Xabr',
        'design': 'selected',
        'content': 'Хабры про дизайн',
    }
    return render(request, 'mainapp/index.html', context = context)


def help(request):
    """ Функция рендерит раздел "Помощь", включая SEO-разметку """

    context = {
        'title': 'Помощь - Xabr',
        'content': 'Краткая документация к сайту',
        'cat_selected': 5
    }
    return render(request, 'mainapp/help.html', context = context)


def LikeView(request, pk):
    """ Функция проставления лайка/дизлайка"""

    post = get_object_or_404(Habr, id = request.POST.get('habr_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
