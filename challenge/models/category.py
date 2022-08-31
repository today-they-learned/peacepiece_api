from django.db import models

from config.models import BaseModel, ModelManager


class CategoryModelManager(ModelManager):
    """Model Manager definition for Category"""

    def get_queryset(self):
        return super().get_queryset().order_by("-display_order")


class Category(BaseModel):
    """Model definition for Category"""

    objects = CategoryModelManager()

    title = models.CharField(
        max_length=50,
    )

    display_order = models.IntegerField()

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
