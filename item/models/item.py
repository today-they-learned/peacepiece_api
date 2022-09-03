from django.db import models

from config.models import BaseModel


class Item(BaseModel):
    """Model definition for Item"""

    CATEGORY_CHOICES = (
    ("map", "map"),
    ("animal","animal"),
    ("item","item"),
)

    name = models.CharField(
        max_length = 30,
    )

    category = models.CharField(
       choices=CATEGORY_CHOICES,
       max_length = 30,
       default = "map",
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
