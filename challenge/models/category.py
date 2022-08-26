from django.db import models

from config.models import BaseModel


class Category(BaseModel):
    """Model definition for Category"""

    title = models.CharField(
        max_length=50,
    )

    display_order = models.IntegerField()
    # TODO: display_order 를 이용한 default scope

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
