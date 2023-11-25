from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a phone number!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    class Type(models.TextChoices):
        LOST = 'LOST',
        FOUND = 'FOUND'

    image = models.ImageField(upload_to='item/')
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=13)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=10,
                            choices=Type.choices,
                            default=Type.LOST)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
