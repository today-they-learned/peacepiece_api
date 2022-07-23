from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self,email,password,username=""):
        if not email:
            raise ValueError(("Users must have an email address"))

        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,password,username=""):
        user = self.create_user(
            email = email,
            username=username,
            password=password,
        )

        user.is_superuser=True
        user.save()

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """Model definition for User."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    username = models.CharField(
         verbose_name = ("username"),
        max_length = 50,
        unique=True,
    )

    email = models.EmailField(
        verbose_name = ("email"),
        max_length=200,
        unique=True,
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