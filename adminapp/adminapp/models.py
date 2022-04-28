from django.db import models
from datetime import datetime

# Create your models here.

class AppRole(models.Model):
    """ Таблица ролей """
    id = models.IntegerField(
        verbose_name='Идентификатор роли',
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Название роли',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание роли',
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.pk}'

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
        db_table = "app_role"
        ordering = ["id"]



class AppFunction(models.Model):
    """ Таблица функций"""
    id = models.IntegerField(
        verbose_name='Идентификатор функции',
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Название функции',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание функции',
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.pk}'

    class Meta:
        verbose_name = 'функция'
        verbose_name_plural = 'функции'
        db_table = "app_function"
        ordering = ["id"]




class RoleFunction(models.Model):
    """ Таблица связи функций и ролей """
    role = models.ForeignKey(  # суффикс _id Django добавит автоматически
        AppRole,
        on_delete=models.CASCADE,
        verbose_name='Ссылка на роль',
    )
    function = models.ForeignKey(  # суффикс _id Django добавит автоматически
        AppFunction,
        on_delete=models.CASCADE,
        verbose_name='Ссылка на функцию',
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'связь функций и ролей'
        db_table = "role_function"
        ordering = ["role", "function"]
        unique_together = (("role", "function"),)


# TBD
    """
     Реализовать:
     1) Таблицу привязок пользователей к ролям 
     2) Метод, проверяющий доступность функции конкретному пользователю.
        Возможно имеет смысл закэшировать все доступные функции.
        is_function_active(user) -> boolean
    """
