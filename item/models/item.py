from django.db import models

from config.models import BaseModel


class Item(BaseModel):
    """Model definition for Item"""

    name = models.CharField(
        max_length = 30,
    )

    thumbnail = models.ForeignKey(
        "file_manager.Image",
        related_name="items",
        on_delete=models.CASCADE,
    )

    point = models.PositiveIntegerField(
        default = 0,
    )

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"
