from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from userapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from .models import User
from .utils import send_verify_mail
from django.conf import settings



def verify(request, user_id, hash):
    user = get_object_or_404(User, pk=user_id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Вы авторизованы, аккаунт активен')
    return render(request, 'userapp/verification.html')


def login(request):
    title = 'вход'
    login_form = UserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))
    context = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'userapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verify_mail(user)
            messages.success(request, 'Проверьте почту!')
            return HttpResponseRedirect(reverse('userapp:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'userapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('help'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data = request.POST, files = request.FILES, instance = request.user)
        profile_form = UserProfileEditForm(data = request.POST, instance = request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = UserProfileForm(instance = request.user)
        profile_form = UserProfileEditForm(instance = request.user.userprofile)
    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'userapp/profile.html', context)
