from django.db import models
from django.urls import reverse
from userapp.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



# Create your models here.


class Ip(models.Model):  # наша таблица где будут айпи адреса
    ip = models.CharField(max_length = 100)

    def __str__(self):
        return self.ip


class Category(models.Model):
    """модель категории поста"""

    objects = None
    name = models.CharField(max_length = 100, unique = True, db_index = True, verbose_name = 'название категории')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    is_active = models.BooleanField(verbose_name = 'активна', default = True)

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})


class Habr(models.Model):
    """ модель хабра (статьи)"""

    objects = None
    title = models.CharField(max_length = 256, blank = False, verbose_name = 'Название статьи')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = "URL")
    content = models.TextField(blank = False, verbose_name = 'Текст статьи')
    images = models.ImageField(upload_to = "images/%Y/%m/%d/", verbose_name = "Картинка")
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = "Время создания")
    time_update = models.DateTimeField(auto_now = True, verbose_name = "Время изменения")
    category = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = "Категория")
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Пользователь')
    is_active = models.BooleanField(default = True, verbose_name = "Активна")
    is_published = models.BooleanField(default = False, verbose_name = "Опубликовано")
    comments = GenericRelation(Comment)

    views = models.ManyToManyField(Ip, related_name = "habr_views", blank = True)

    class Meta:
        verbose_name = "Хабр"
        verbose_name_plural = "Хабры"
        ordering = ('-time_create', 'title')

    def __str__(self):
        return self.title
        # return f"{self.short_description} ({self.category.name} {self.is_active} {self.slug} {self.id_user})"

    def get_absolute_url(self):
        return reverse('post', kwargs = {'habr_slug': self.slug})

    def total_views(self):
        return self.views.count()


class HabrLike(models.Model):
    """ Таблица лайков к хабру """

    user = models.ForeignKey(User,
                             on_delete = models.CASCADE,
                             verbose_name = 'Ссылка на пользователя'
                             )
    habr = models.ForeignKey(Habr,
                             on_delete = models.CASCADE,
                             verbose_name = 'Ссылка на хабр'
                             )

    created = models.DateTimeField(auto_now_add = True, editable = False)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        db_table = "habr_like"


def get_absolute_url(self):
    return reverse('post_detail_url', kwargs={'slug': self.slug})
