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
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    STATUSES = (
        (1, 'Черновик'),
        (2, 'Одобрено'),
        (3, 'Отказано')
    )
    status = models.IntegerField(verbose_name='Статус модерирования', choices=STATUSES, blank=False, default=1)


class HabrLike(models.Model):
    """ Таблица лайков к хабру """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Ссылка на пользователя'
                             )
    habr = models.ForeignKey(Habr,
                             on_delete=models.CASCADE,
                             verbose_name='Ссылка на хабр'
                             )

    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        db_table = "habr_like"

