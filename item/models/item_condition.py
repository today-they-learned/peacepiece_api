from django.db import models

from config.models import BaseModel


class ItemCondition(BaseModel):
    """Model definition for ItemCondition"""

    item = models.ForeignKey(
        "item.Item",
        related_name="conditions",
        on_delete=models.CASCADE,
    )

    pre_item_condition = models.ForeignKey(
        "item.ItemCondition",
        null=True,
        blank=True,
        related_name="conditions",
        on_delete=models.SET_NULL,
    )

    max_count = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        db_table = "item_conditions"
        verbose_name = "ItemCondition"
        verbose_name_plural = "ItemConditions"
