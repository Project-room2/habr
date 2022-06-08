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

def verify(request, email, activation_key):
    """
    If the user exists, and the activation key is valid, then activate the user and log them in

    :param request: The current request object
    :param email: The email address of the user who is trying to verify their account
    :param activation_key: The activation key that was sent to the user
    :return: a response object.
    """
    try:
        user = User.objects.get(email=email)
        if user.activation_key == hash and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = None
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Вы авторизованы, аккаунт активен')
            return render(request, 'userapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'userapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('index'))

def login(request):
    """
    If the user is submitting a login form, authenticate the user and log them in

    :param request: The request object is the first parameter to every Django view function. It contains information about
    the current request, such as the client’s machine details, the URI that was requested, and much more
    :return: A dictionary with the title, login_form, and next variables.
    """
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
                return HttpResponseRedirect(reverse('help'))
    context = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'userapp/login.html', context)


def register(request):
    """
    If the request method is POST, then validate the form and save the user, otherwise create an empty form

    :param request: The current request object
    :return: a render object.
    """
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # send_verify_mail(user)
            # messages.success(request, 'Проверьте почту!')
            return HttpResponseRedirect(reverse('userapp:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'userapp/register.html', context)


def logout(request):
    """
    It logs the user out and redirects them to the help page

    :param request: The request object is a Python object that contains metadata about the request sent to the server
    :return: The user is being logged out and redirected to the help page.
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('help'))


@login_required
def profile(request):
    """
    If the request is a POST request, then validate the form and save the form. If the request is a GET request, then render
    the form

    :param request: The request object is a Python object that contains information about the current request
    :return: The user's profile page.
    """
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