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

    name = models.CharField(verbose_name='название категории', max_length=64, default='', unique=True)
    slug = models.SlugField(verbose_name='уникальный адрес', max_length=70)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Habr(models.Model):
    """ модель хабра (статьи)"""

    Design = '1'
    Web_development = '2'
    Mobile_development = '3'
    Marketing = '4'

    SUBJECT_CHOICES = (
        (Design, 'Дизайн'),
        (Web_development, 'Веб-разработка'),
        (Mobile_development, 'Мобильная разработка'),
        (Marketing, 'Маркетинг'),
    )
    short_description = models.CharField(verbose_name = 'Название статьи', max_length = 256, blank = False)
    description = models.TextField(verbose_name = 'Текст статьи', blank = False)
    created_timestamp = models.DateTimeField(auto_now_add = True, db_index = True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    is_published = models.BooleanField(default = False)
    slug = models.SlugField(verbose_name = 'Уникальный адрес', max_length = 70, unique = True)

    STATUSES = (
        (1, 'Черновик'),
        (2, 'Одобрено'),
        (3, 'Отказано')
    )
    status = models.IntegerField(verbose_name = 'Статус модерирования', choices = STATUSES, blank = False, default = 1)

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ('-created_timestamp',)

    def __str__(self):
        return f"{self.short_description} ({self.category.name} {self.is_active} {self.slug} {self.id_user})"

    def get_absolute_url(self):
        return reverse('blogapp:post_list')

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



