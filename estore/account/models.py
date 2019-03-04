from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None, is_staff=False, is_active=True,
            **extra_fields):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff,
            **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields)


class UserInfo(models.Model):
    name = models.CharField(max_length=256, blank=True)
    qq = models.CharField(
        max_length=15, blank=True, unique=True,
        null=True, verbose_name='QQ号码')
    mobile = models.CharField(
        max_length=11, blank=True, null=True,
        unique=True, verbose_name='手机号码')

    # email = models.EmailField(unique=True)
    # company_name = models.CharField(max_length=256, blank=True)
    # address_detail = models.CharField(max_length=256, blank=True)
    # hobby =
    # profession =
    # birthday =
    # nick_name =
    # head_portrait =
    # gender =

    def __str__(self):
        return self.name


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    user_info = models.OneToOneField(
        UserInfo, null=True, blank=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
