from challenge.models import Category
from config.serializers import BaseModelSerializer
from rest_framework import serializers


class CategorySerializer(BaseModelSerializer):
    """Serializer definition for Category Model."""

    class Meta:
        """Meta definition for CategorySerializer."""

        model = Category
        fields = [
            "id",
            "title",
            "display_order",
        ]

        read_only_fields = [
            "id",
            "title",
            "display_order",
        ]
