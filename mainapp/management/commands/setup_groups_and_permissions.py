from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from userapp.models import User # мы переопредели модель пользователя, поэтому импортируем именно отсюда
# import logging
from django.db import IntegrityError

#  Перечень групп и их разрешений для работы с приложениями проекта
GROUPS = {
    "Administrator": {
        # Основные разрешения
        "log entry": ["add", "delete", "change", "view"],
        "group": ["add", "delete", "change", "view"],
        "permission": ["add", "delete", "change", "view"],
        "user": ["add", "delete", "change", "view"],
        "content type": ["add", "delete", "change", "view"],
        "session": ["add", "delete", "change", "view"],

        # Разрешения для конкретных моделей
        "habr": ["add", "delete", "change", "view"],
        "habrlike": ["add", "delete", "change", "view"],
    },

    "Moderator": {
        # Разрешения для конкретных моделей
        "habr": ["add", "delete", "view"]
    },

    "Member": {
        # Разрешения для конкретных моделей
        "habr": ["add", "delete", "change", "view"],
        "habrlike": ["add", "delete", "change", "view"],
    },

    "Guest": {
        # Разрешения для конкретных моделей
        "habr": ["view"],
        "habrlike": ["view"],
    },

}

USERS = {
    "admin": ["Administrator", "test_admin@yandex.ru", "1234"],
    "user_moderator": ["Moderator", "test_moderator@yandex.ru", "1234"],
    "user_member": ["Member", "test_member@yandex.ru", "1234"],
    "user_guest": ["Guest", "test_quest@yandex.ru", "1234"],
}


class Command(BaseCommand):
    """Создание унифицированных групп и разрешений по умолчанию для тестирования проекта"""

    def handle(self, *args, **options):

        for group_name in GROUPS:

            new_group, created = Group.objects.get_or_create(name=group_name)

            # Loop models in group
            for app_model in GROUPS[group_name]:

                # Loop permissions in group/model
                for permission_name in GROUPS[group_name][app_model]:

                    # Generate permission name as Django would generate it
                    name = f"Can {permission_name} {app_model}"
                    print(f"Creating {name}")

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning(f"Permission not found with name '{name}'.")
                        continue

                    new_group.permissions.add(model_add_perm)

            for user_name in USERS:

                new_user = None
                try:
                    if user_name == "admin":
                        new_user, created = User.objects.get_or_create(username=user_name, is_staff=True, is_superuser=True,
                                                                       email=USERS[user_name][1])
                    else:
                        new_user, created = User.objects.get_or_create(username=user_name, is_staff=True,
                                                                       email=USERS[user_name][1])

                    new_user.set_password(USERS[user_name][2])
                    new_user.save()

                except IntegrityError:
                    new_user = User.objects.get(username=user_name)


                if USERS[user_name][0] == str(new_group):
                    new_group.user_set.add(new_user)

                    print(f"Adding {user_name} to {new_group}")
