import userapp.models
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import DetailView, ListView
from .models import *


def page_not_found_view(request, exception):
    """
    It renders the 404.html template, passing in the path of the requested page

    :param request: The request object
    :param exception: The exception raised by the view function
    :return: The render function is being returned.
    Question: What is the render function doing?
    Answer: The render function is taking the request, the template, and the status.
    Question: What is the template?
    Answer: The template is the 404.html file.
    Question: What is the status?
    Answer: The status is 404.
    Question: What is the path?
    """
    return render(request, 'mainapp/404.html', {'path': request.path}, status = 404)


class IndexView(ListView):
    """ Контроллер, отображает все активныее и разрешениые к публикации Хабры на главной """

    paginate_by = 4
    model = Habr
    allow_empty = True
    template_name = 'mainapp/index.html'
    context_object_name = 'habrs'


    def get_queryset(self):
        """
        Отрисовываем главную страницу, если была задействована форма поиска - результат поиска по всем хабрам
        If the user has searched for something, return the results of the search.
        Otherwise, return the default posts
        :return: The get_queryset() method is being returned.
        """

        search_post = self.request.GET.get('search')
        if search_post:
                posts = Habr.objects.filter(Q(title__icontains = search_post) | Q(content__icontains = search_post), is_published = True, is_active = True)
        else:
            # If not searched, return def   ault posts
            posts = Habr.objects.filter(is_published = True, is_active = True)
        return posts

    def get_context_data(self, *, object_list = None, **kwargs):
        """
        The function takes in a list of objects, and returns a dictionary of context

        :param object_list: The list of objects. If not provided, this will default to model.objects.all()
        :return: The context is a dictionary mapping template variable names to Python objects.
        """

        context = super().get_context_data()

        context['title'] = 'Xabr - знания это сила!'
        context['cat_selected'] = 0
        context['art'] = Habr.objects.filter(is_published = True, is_active = True).order_by('-habr_view')[:5]
        context['art_like'] = Habr.objects.filter(is_published = True, is_active = True)
        context['art_author'] = Habr.objects.filter(is_published = True, is_active = True)
        return context


class SectionView(ListView):
    """ Контроллер, отборажает активные и разрешенные к публикации Хабры выбранного раздела """

    model = Habr
    paginate_by = 4
    allow_empty = True
    template_name = 'mainapp/habr_list.html'
    context_object_name = 'habr'


    def get_queryset(self):
        """
        Отрисовываем раздел, если была задействована форма поиска - результат поиска по всем хабрам
        If the user has searched for something, return the results of the search.
        Otherwise, return the default posts
        :return: The queryset is being returned.
        """

        search_post = self.request.GET.get('search')
        if search_post:
            posts = Habr.objects.filter(Q(title__icontains = search_post) | Q(content__icontains = search_post), is_published = True, is_active = True)
        else:
            # If not searched, return def   ault posts
            posts = Habr.objects.filter(category__slug = self.kwargs['cat_slug'], is_published = True, is_active = True)
        return posts


    def get_context_data(self, *, object_list = None, **kwargs):
        """
        The function takes in a list of objects and returns a dictionary of context data

        :param object_list: The list of objects that the view is operating upon
        :return: The context is being returned.
        """

        context = super().get_context_data(**kwargs)
        if len(context['habr']) > 0:
            cat_selected = context['habr'][0].category.id
            context['title'] = str(context['habr'][0].category) + ' - Xabr '
            context['cat_selected'] = context['habr'][0].category.id
            context['art'] = Habr.objects.filter(is_published = True, is_active = True,
                                                 category = cat_selected).order_by('-habr_view')[:5]
            context['author'] = Habr.objects.filter(category = cat_selected).order_by().values('user').distinct()
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


class UserView(DetailView):
    """ Функция публичного профиля автора Хабра  """

    template_name = 'mainapp/profile.html'
    model = User
    context_object_name = 'profile'
    paginate_by = 4
    allow_empty = True


    def get_context_data(self, **kwargs):
        """
        Выбираем Хабры автора для публичного профиля автора
        The function get_context_data() is a method of the DetailView class.
        called by the DetailView class when it needs to get the context data for the template.
        The context data is a dictionary of data that is passed to the template.
        The context data is used by the template to render the page.
        The context data is passed to the template by the DetailView class.
        The DetailView class calls the get_context_data() method to get the context data.
        The get_context_data() method is defined in the DetailView class.
        The DetailView class is a subclass of the View class.
        The View class is a subclass of the object class.
        The object class is the base class for all classes.
        The get_context_data() method is defined in the DetailView class.
        The DetailView class is a subclass of the View class
        :return: The context is being returned.
        """
        context = super().get_context_data(**kwargs)
        context['habrs'] = Habr.objects.filter(user_id=context['object'].id).order_by('-time_update')
        context['title'] = 'Профиль автора Хабров'
        return context

def design(request):
    """
    Функция рендерит раздел "Дизайн", включая SEO-разметку
    It renders the "Design" section, including SEO markup

    :param request: The request object is an instance of HttpRequest. It contains metadata about the request, such as the
    client’s IP address, the URI that was requested, the HTTP method, and so on
    :return: the rendered template with the context.
    """

    context = {
        'title': 'Дизайн - Xabr"',
        'design': 'selected',
        'content': 'Хабры по дизайну',
    }
    return render(request, 'mainapp/index.html', context = context)


def web_dev(request):
    """
    Функция рендерит раздел "Веб-разработку", включая SEO-разметку
    It renders the "Web Development" section, including SEO markup

    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :return: a render() function, which is a shortcut for a few things:
    """

    context = {
        'title': 'Веб-разработка - Xabr"',
        'web_dev': 'selected',
        'content': 'Хабры по Веб-разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def mobile_developing(request):
    """
    Функция рендерит раздел "Мобильная разработка", включая SEO-разметку
    It renders the "Mobile Development" section, including SEO markup

    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :return: a response object.
    """

    context = {
        'title': 'Мобильная разработка - Xabr',
        'mobile_developing': 'selected',
        'content': 'Хабры по Мобильной разработке',
    }
    return render(request, 'mainapp/index.html', context = context)


def marketing(request):
    """
    Функция рендерит раздел "Маркетинг", включая SEO-разметку
    It renders the "Marketing" section, including SEO markup

    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :return: a response object.
    """

    context = {
        'title': 'Дизайн - Xabr',
        'design': 'selected',
        'content': 'Хабры про дизайн',
    }
    return render(request, 'mainapp/index.html', context = context)


def help(request):
    """
    Функция рендерит раздел "Помощь", включая SEO-разметку
    It renders the "Help" section, including SEO markup

    :param request: The initial request
    :return: a response object with the rendered template.
    """

    context = {
        'title': 'Помощь - Xabr',
        'content': 'Краткая документация к сайту',
        'cat_selected': 5
    }
    return render(request, 'mainapp/help.html', context = context)


def LikeView(request, pk):
    """
    Функция проставления лайка/дизлайка
    If the user has already liked the post, remove the like; otherwise, add a like

    :param request: The request object is the first parameter to all Django views. It contains metadata about the request,
    such as the HTTP method ("GET" or "POST"), the client's IP address, the query parameters, and more
    :param pk: The primary key of the post that we want to like
    :return: the HTTP response with the status code 302.
    """

    post = get_object_or_404(Habr, id = request.POST.get('habr_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
