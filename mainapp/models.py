from django.db import models
from userapp.models import User

# Create your models here.


class Habr(models.Model):
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
    short_description = models.CharField(verbose_name='Название статьи',max_length=256, blank=False)
    description = models.TextField(verbose_name='Текст статьи', blank=False)
    created_timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    id_category = models.CharField(verbose_name='Тема', max_length=1, choices=SUBJECT_CHOICES, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL())
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
