from django.contrib import admin
from point.models import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    """Admin View for Point"""

    list_display = (
        "pointable_type",
        "pointable_id",
        "amount",
    )
