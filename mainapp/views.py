from django.shortcuts import render

def index(request):
    context = {
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
