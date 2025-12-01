from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from apps.common.models import TImeStampedUUIDModel
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, passwoed=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password = (passwoed)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, extra_fields)

class User(AbstractBaseUser, PermissionsMixin, TImeStampedUUIDModel):
    email = models.CharField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # login with email not username
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email