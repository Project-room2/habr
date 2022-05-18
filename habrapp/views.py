from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from pytils.translit import slugify
from mainapp.models import Habr
from .forms import HabrEditForm


def habr_create(request):

    newpk = None
    if request.method == 'POST':

        form = HabrEditForm(data=request.POST)
        if 'do_publish' in request.POST:
            id = int(request.POST.get('do_publish', None))
            habr = get_object_or_404(Habr, pk=id)
            habr.is_published = True
            habr.time_update = timezone.now()
            habr.save(update_fields=["is_published", "time_update"])
            may_published = False

        else:
            if form.is_valid():
                habr = form.save(commit=False)
                habr.user = request.user
                habr.is_published = False
                habr.is_active = True
                habr.slug = slugify(habr.title)
                if habr.pk is None:
                    habr.time_create = timezone.now()
                habr.time_update = timezone.now()
                habr.save()
                may_published = True
                newpk = habr.pk
                #  return HttpResponseRedirect(reverse('habrapp:create'))
    else:
        form = HabrEditForm(data=request.POST)
        may_published = False

    context = {
        'form': form,
        'may_published': may_published,
        'newpk': newpk
    }
    return render(request, 'mainapp/habr_edit.html', context)
