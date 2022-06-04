from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from userapp.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from taggit.managers import TaggableManager


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
    content = RichTextUploadingField(blank = False, verbose_name = 'Текст статьи')
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = "Время создания")
    time_update = models.DateTimeField(auto_now = True, verbose_name = "Время изменения")
    category = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = "Категория")
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Пользователь')
    is_active = models.BooleanField(default = True, verbose_name = "Активна")
    is_published = models.BooleanField(default = False, verbose_name = "Опубликовано")
    likes = models.ManyToManyField(User, related_name = 'blog_post')
    like_quantity = models.PositiveIntegerField('кол-во', default = 0)
    habr_view = models.IntegerField('просмотров', default = 1)
    comments = GenericRelation(Comment)
    is_ask_published = models.BooleanField(default=False, verbose_name="Запрошена публикация")

    class Meta:
        verbose_name = "Хабр"
        verbose_name_plural = "Хабры"
        ordering = ('-time_create', 'title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs = {'habr_slug': self.slug})
        return reverse('post')

    def total_likes(self):
        return self.likes.count()

    tags = TaggableManager()

class Like(models.Model):
    """модель лайков к постам"""
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    is_active = models.BooleanField(verbose_name = 'активна', default = True)

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "лайки"
