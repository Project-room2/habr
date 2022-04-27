from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import *


# class HabrsView(ListView):
#     model = Habr
#     template_name = 'mainapp/index.html'
#
#     def get_queryset(self):
#         return Habr.objects.filter(is_active = True)


class SectionView(ListView):
    model = Habr
    allow_empty = False
    template_name = 'mainapp/habr_list.html'

    def get_queryset(self):
        return Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True)

        # return Habr.objects.filter(category = 1, is_published = True)


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


def habr(request, slug):
    """контроллер вывода хабра"""

    habr = Habr.objects.filter(slug = slug, is_active = True)
    categories = Category.objects.all()

    # post = Habr.objects.filter(slug = slug, is_active = True)
    # categories = Habr.category.objects.all()
    # comment = Comments.objects.filter(post=post.first())

    # if request.method == "POST":
    #     form = CommentForm(data=request.POST)
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.user = request.user
    #         form.post = post.first()
    #         form.save()
    #
    # else:
    #     form = CommentForm()

    context = {
        'page_title': 'хабр',
        'habrs': habr,
        'title': 'Хабр',
        'content': 'Выбранный хабр',
        'categories': categories,
        # 'comments': comment,
        # 'form': form,
    }
    return render(request, 'mainapp/habr.html', context)


# def section(request, slug):
#     """контроллер вывода страниц статей, относящихся к конкретной категории """
#
#     categories = Category.objects.filter(is_active = True)
#     category = get_object_or_404(Category, slug = slug)
#     cat = Habr.category
#     posts = Habr.objects.filter(Category = '1').order_by('-time_create')
#
#     # if request.user.is_authenticated:
#     #     new_like, created = Like.objects.get_or_create(
#     #         user=request.user, slug=slug)
#     # else:
#     #     new_like = Like.objects.all()
#     # if slug == '':
#     #     category = {'slug': '', 'name': 'все'}
#     #     posts = Post.objects.filter(
#     #         is_active=True).order_by('-create_datetime')
#     # else:
#     #     category = get_object_or_404(Category, slug=slug)
#     #     posts = category.post_set.filter(
#     #         is_active=True).order_by('-create_datetime')
#
#     context = {
#         'page_title': 'главная',
#         'categories': categories,
#         'category': category,
#         'posts': posts,
#         'content': category,
#         'cat': cat,
#         #     'new_like': new_like,
#     }
#     return render(request, 'mainapp/section.html', context)
