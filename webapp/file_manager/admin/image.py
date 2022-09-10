from django.contrib import admin
from file_manager.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Admin View for Image"""

    list_per_page = 10
    list_display = (
        "id",
        "file",
    )
    ordering = ("created_at", "updated_at")
