from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from userapp.models import User
from django.template import defaultfilters
from django.utils.text import slugify
import random
import string


# Create your models here.


class Category(models.Model):
    """модель категории поста"""

    objects = None
    name = models.CharField(max_length = 100, unique = True, db_index = True, verbose_name = 'название категории')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})



class Habr(models.Model):
    """ модель хабра (статьи)"""

    objects = None
    title = models.CharField(max_length = 256, blank = False, verbose_name = 'Название статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank = False, verbose_name = 'Текст статьи')
    # photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = "Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    # id_user = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'ID ползователя')
    is_active = models.BooleanField(default = True, verbose_name = "Активна")
    is_published = models.BooleanField(default=False, verbose_name="Публикация")

    class Meta:
        verbose_name = "Хабры"
        verbose_name_plural = "Хабры"
        ordering = ('-time_create', 'title')

    def __str__(self):
        return self.title
        # return f"{self.short_description} ({self.category.name} {self.is_active} {self.slug} {self.id_user})"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

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
    verbose_name = 'habrlike'
    verbose_name_plural = 'habrlikes'
    db_table = "habr_like"



