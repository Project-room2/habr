from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from pytils.translit import slugify
from mainapp.models import Habr
from .forms import HabrEditForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from taggit.models import Tag


@login_required
def habr_publish(request, habr_slug):
    """ Функция установки признака "Запрос на публикацию" на хабре """
    habr = get_object_or_404(Habr, slug=habr_slug)
    habr.is_ask_published = True
    habr.time_update = timezone.now()
    habr.save()
    return HttpResponseRedirect(reverse('habrapp:myhabrlist'))

@login_required
def habr_remove(request, habr_slug):
    """ Функция удаления хабра"""
    habr = get_object_or_404(Habr, slug=habr_slug)
    habr.is_active = False
    habr.time_update = timezone.now()
    habr.save()
    return HttpResponseRedirect(reverse('habrapp:myhabrlist'))

@login_required
def habr_restore(request, habr_slug):
    """ Функция восстановления хабра"""
    habr = get_object_or_404(Habr, slug=habr_slug)
    habr.is_active = True
    habr.time_update = timezone.now()
    habr.save()
    return HttpResponseRedirect(reverse('habrapp:myhabrlist'))


class HabrEdit(UpdateView):
    """Контроллер редактирования хабра"""
    model = Habr
    template_name = "mainapp/habr_edit.html"
    slug_url_kwarg = 'habr_slug'
    form_class = HabrEditForm
    success_url = reverse_lazy('habrapp:myhabrlist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование хабра'
        context['edit'] = True
        return context

@login_required
def habr_create(request):
    """ Функция создания  хабра"""

    newpk = None
    save_is_active = True
    if request.method == 'POST':

        form = HabrEditForm(data=request.POST)
        if 'do_publish' in request.POST:
            id = int(request.POST.get('do_publish', None))
            habr = get_object_or_404(Habr, pk=id)
            habr.is_ask_published = True
            habr.time_update = timezone.now()
            habr.save(update_fields=["is_active", "time_update"])
            may_published = False
            save_is_active = False
        else:
            if form.is_valid():
                habr = form.save(commit=False)
                habr.user = request.user
                habr.is_published = False
                habr.is_active = False
                habr.slug = slugify(habr.title)
                if habr.pk is None:
                    habr.time_create = timezone.now()
                habr.time_update = timezone.now()
                habr.is_active = True
                habr.save()
                may_published = True
                newpk = habr.pk
                return HttpResponseRedirect(reverse('habrapp:myhabrlist'))
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = HabrEditForm(data=request.POST)
        may_published = False


    context = {
        'form': form,
        'may_published': may_published,
        'newpk': newpk,
        'save_is_active': save_is_active
    }
    return render(request, 'mainapp/habr_edit.html', context)

class HabrListView(ListView):
    """ Контроллер, отображает все Хабры текущего пользователя """

    model = Habr
    paginate_by = 4
    allow_empty = True
    template_name = 'mainapp/user_habr_list.html'
    context_object_name = 'habr'


    def get_queryset(self):
        """ Определяем все хабры текущего пользователя """
        posts = Habr.objects.filter(user = self.request.user).order_by('-time_update')
        return posts


    # def get_context_data(self, *, object_list = None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if len(context['habr']) > 0:
    #         cat_selected = context['habr'][0].category.id
    #         context['title'] = str(context['habr'][0].category) + ' - Xabr '
    #         context['cat_selected'] = context['habr'][0].category.id
    #         context['art'] = Habr.objects.filter(is_published = True, is_active = True,
    #                                              category = cat_selected).order_by('-habr_view')[:5]
    #         context['author'] = Habr.objects.filter(category = cat_selected).order_by().values('user').distinct()
    #     else:
    #         context['title'] = ''
    #         context['cat_selected'] = ''
    #     return context
