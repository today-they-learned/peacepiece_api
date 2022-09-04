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

    def is_buyable(self, user_owned_items):
        user_owned_item = user_owned_items.filter(item=self.item).first()

        if user_owned_item and user_owned_item.count >= self.max_count:
            return False

        pre_item_condition = self.pre_item_condition

        if pre_item_condition:
            user_owned_pre_condition_item = user_owned_items.filter(item=pre_item_condition.item).first()
            if user_owned_pre_condition_item is None:
                return False
            if user_owned_pre_condition_item.count < pre_item_condition.max_count:
                return False

        return True
