from config.models import BaseModel
from django.db import models


class UserItem(BaseModel):
    """Model definition for UserItem"""

    user = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_items",
    )

    item = models.ForeignKey(
        "item.Item",
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_items",
        blank=True,
    )

    count = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        db_table = "user_items"
        verbose_name = "UserItem"
        verbose_name_plural = "UserItems"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "item"],
                name="unique_item_by_user",
            )
        ]
