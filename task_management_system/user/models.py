from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, age, password=None, **extra_fields):
        if not email:
            raise ValueError('This field is required.')

        if not age:
            raise ValueError('This field is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, age=age, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, age, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('"is_staff" must be set to True for superuser.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('"is_superuser" must be set to True for superuser.')

        return self.create_user(email, username, age, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    MAX_FIRST_NAME_LENGTH = 64
    MAX_LAST_NAME_LENGTH = 64
    MAX_USERNAME_LENGTH = 64
    MAX_EMAIL_LENGTH = 128

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        unique=True
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True
    )

    age = models.PositiveIntegerField()

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True
    )

    image = models.ImageField(
        default='no pic.jpg',
        upload_to='user_images',

    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
