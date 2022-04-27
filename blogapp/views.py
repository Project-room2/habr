from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mainapp.models import Habr


class BlogListView(ListView):
    """класс для вывода списка всех статей пользователя"""

    model = Habr
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    """класс для вывода черновиков пользователя"""

    model = Habr
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    """класс для вывода страницы создания новой статьи пользователем"""

    model = Habr
    template_name = 'post_new.html'
    fields = ['user', 'category', 'name', 'description', 'posts_text', 'is_active']


class BlogUpdateView(UpdateView):
    """класс для вывода страницы редактирования статьи/черновика пользователем"""

    model = Habr
    template_name = 'post_edit.html'
    fields = ['category', 'name', 'description', 'posts_text', 'is_active']


class BlogDeleteView(DeleteView):
    """класс для вывода страницы удаления статьи/черновика пользователем"""

    model = Habr
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:post_list')
