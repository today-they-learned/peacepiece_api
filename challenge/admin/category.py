from django.contrib import admin

from challenge.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin View for Category"""

    list_display = (
        "id",
        "title",
    )

    ordering = ("display_order",)
