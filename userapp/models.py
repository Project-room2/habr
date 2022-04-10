from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def default_expire_time():
    return now() + timedelta(hours=48)

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=18)

    activation_key = models.CharField(max_length=64, blank=True, null=True)

    activation_key_expires = models.DateTimeField(default=default_expire_time)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    id_user_category = models.ForeignKey(user_category, on_delete=models.SET_NULL())
