from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as lazy_text
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.conf import settings

#User = settings.AUTH_USER_MODEL



# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email, username, password=None, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.username = username
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staff_user(self, email, username, password=None):
        user = self.create_user(
            email, username, password,
            is_staff=True)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email, username, password, is_staff=True,
            is_superuser=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, unique=True, blank=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()