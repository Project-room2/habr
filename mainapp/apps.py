from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'


class InterstoreAppConfig(AppConfig):
    """ присвоение verbose_name приложению mainapp в административной панели"""

    name = "mainapp"
    verbose_name = "Главное приложение"

