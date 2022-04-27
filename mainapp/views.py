from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

import slug as slug
from django.shortcuts import get_object_or_404, render
from .models import Category, Habr


def index(request):
    """контроллер, возврящающий главную страницу со списком всех статей сайта"""

    habr = Habr.objects.filter(is_active = True).order_by('-created_timestamp')
    habrs = Habr.objects.all()
    categories = Habr.category

    context = {
        'habr': habr,
        'habrs': habrs,
        'title': 'Главная',
        'index': 'selected',
        'content': 'Все потоки хабров',
    }
    return render(request, 'mainapp/index.html', context)


def design(request):
    context = {
        'title': 'Дизайн',
        'design': 'selected',
        'content': 'Хабры по дизайну',
    }
    return render(request, 'mainapp/index.html', context)


def web_developing(request):
    context = {
        'title': 'Веб-разработка',
        'web_developing': 'selected',
        'content': 'Хабры по Веб-разработке',
    }
    return render(request, 'mainapp/index.html', context)


def mobile_developing(request):
    context = {
        'title': 'Мобильная разработка',
        'mobile_developing': 'selected',
        'content': 'Хабры по Мобильной разработке',
    }
    return render(request, 'mainapp/index.html', context)


def marketing(request):
    context = {
        'title': 'Маркетинг',
        'marketing': 'selected',
        'content': 'Хабры по Маркетингу',
    }
    return render(request, 'mainapp/index.html', context)


def help(request):
    context = {
        'title': 'Помощь',
        'help': 'selected',
        'content': 'Краткая документация к сайту',
    }
    return render(request, 'mainapp/index.html', context)


def habr(request, slug):
    """контроллер вывода хабра"""

    habr = Habr.objects.filter(slug=slug, is_active=True)
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


def section(request, slug):
    """контроллер вывода страниц статей, относящихся к конкретной категории """

    categories = Category.objects.filter(is_active=True)
    category = get_object_or_404(Category, slug = slug)
    posts = Habr.objects.filter(category = '1').order_by('-created_timestamp')


    # if request.user.is_authenticated:
    #     new_like, created = Like.objects.get_or_create(
    #         user=request.user, slug=slug)
    # else:
    #     new_like = Like.objects.all()
    # if slug == '':
    #     category = {'slug': '', 'name': 'все'}
    #     posts = Post.objects.filter(
    #         is_active=True).order_by('-create_datetime')
    # else:
    #     category = get_object_or_404(Category, slug=slug)
    #     posts = category.post_set.filter(
    #         is_active=True).order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'categories': categories,
        'category': category,
        'posts': posts,
        'content': category,
   #     'new_like': new_like,
    }
    return render(request, 'mainapp/section.html', context)
