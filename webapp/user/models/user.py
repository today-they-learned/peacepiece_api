import random

from config.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.files import File
from django.db import models

AVATAR_IMAGE_COUNT = 21

RANDOM_PROFILE = [f"avatars/{idx + 1}.jpg" for idx in range(AVATAR_IMAGE_COUNT)]


def get_random_profile_filename():
    return random.choice(RANDOM_PROFILE)


def user_avatar_upload_path(instance, filename):
    return "avatars/user_{}/{}".format(instance.username, filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password, username=""):
        if not email:
            raise ValueError(("Users must have an email address"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, username=""):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """Model definition for User."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    username = models.CharField(
        verbose_name=("username"),
        max_length=50,
        unique=True,
    )

    email = models.EmailField(
        verbose_name=("email"),
        max_length=200,
        unique=True,
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        verbose_name="프로필 이미지",
        upload_to=user_avatar_upload_path,
    )

    items = models.ManyToManyField(
        "item.Item",
        related_name="users",
        through="item.UserItem",
    )

    point = models.IntegerField(
        default=0,
        null=False,
        verbose_name="소지 포인트",
    )

    reminder_categories = models.ManyToManyField(
        "challenge.Category",
        related_name="users",
        through="challenge.ChallengeReminder",
    )

    objects = UserManager()

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self) -> str:
        return f"[{self.id}] {self.username} ({self.email})"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            filename = get_random_profile_filename()
            f = open("staticfiles/" + filename, "rb")
            self.avatar = File(f)
        super().save(force_insert, force_update, using, update_fields)
