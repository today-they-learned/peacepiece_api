from django.db import models

from config.models import BaseModel


class Item(BaseModel):
    """Model definition for Item"""

    CATEGORY_CHOICES = (
        ("map", "map"),
        ("animal", "animal"),
        ("item", "item"),
    )

    name = models.CharField(
        max_length=30,
        verbose_name="아이템명",
    )

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default="map", verbose_name="아이템 종류")

    thumbnail = models.ForeignKey(
        "file_manager.Image", related_name="items", on_delete=models.CASCADE, verbose_name="아이템 이미지"
    )

    point = models.PositiveIntegerField(default=0, verbose_name="아이템 가격")

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self) -> str:
        return f"[{self.id}] {self.name}"
