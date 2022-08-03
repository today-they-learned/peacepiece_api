from django.db import models
from user.models import User


class Notification(models.Model):
    """Model definition for Notification"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notification",
    )
    category = models.IntegerField()
    notifiable_type = models.TextField(
        null=True,
        blank=True,
    )
    notifiable_id = models.IntegerField(
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "notification"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
