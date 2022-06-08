from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from adminapp.models import AppRole


def default_expire_time():
    """
    It returns the current time plus 48 hours
    :return: A datetime object that is 48 hours in the future.
    """
    return now() + timedelta(hours=48)


class User(AbstractUser):
    # Creating a user profile.
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=18)
    activation_key = models.CharField(max_length=64, blank=True, null=True)
    activation_key_expires = models.DateTimeField(default=default_expire_time)


    def get_absolute_url(self):
        """
        It returns the URL of the avatar view, which is the view that will display the avatar.
        :return: The url of the avatar page.
        """
        return reverse('avatar')

    def is_activation_key_expired(self):
        """
        If the current time is less than the expiration time, return False, otherwise return True
        :return: The function is_activation_key_expired is being returned.
        """
        if now() <= self.activation_key_expires:
            return False
        return True

    def get_full_name(self):
        """
        If the user has a full name, return it, otherwise return the username
        :return: The username if the full name is empty, otherwise the full name.
        """
        fio = super().get_full_name()
        if fio == "":
            return self.username
        return fio


class UserProfile(models.Model):
    # The UserProfile class is a one-to-one relationship with the User class.
    # It has a few extra fields, and a few extra methods
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='метки', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        If a user is created, create a UserProfile object with the user attribute set to the newly created user

        :param sender: The model class
        :param instance: The User instance that was just created
        :param created: A boolean; True if a new record was created
        """
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        "When a User object is saved, save the UserProfile object associated with it."

        The first argument, sender, is the model class. The instance argument is the actual instance being saved

        :param sender: The model class
        :param instance: The User instance being saved
        """
        instance.userprofile.save()