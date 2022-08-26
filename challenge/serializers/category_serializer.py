from rest_framework import serializers

from challenge.models import Category


class CategorySerializer(serializers.ModelSerializer):
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
