from config.models import BaseModel, ModelManager
from django.db import models


class ItemModelManager(ModelManager):
    """Model Manager definition for Category"""

    def get_queryset(self):
        return super().get_queryset().order_by("-display_order")


class Item(BaseModel):
    """Model definition for Item"""

    CATEGORY_CHOICES = (
        ("map", "map"),
        ("animal", "animal"),
        ("item", "item"),
        ("tree", "tree"),
    )

    name = models.CharField(
        max_length=30,
        verbose_name="아이템명",
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=30,
        default="map",
        verbose_name="아이템 종류",
    )

    thumbnail = models.ForeignKey(
        "file_manager.Image",
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="아이템 이미지",
    )

    point = models.PositiveIntegerField(
        default=0,
        verbose_name="아이템 가격",
    )

    display_order = models.IntegerField(
        default=0,
        verbose_name="표시 순서",
    )

    objects = ItemModelManager()

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self) -> str:
        return f"[{self.id}] {self.name}"
