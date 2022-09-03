from rest_framework import serializers

from file_manager.serializers import ImageSerializer
from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Serializer definition for Item Model."""

    thumbnail = ImageSerializer(read_only=True)

    is_gettable = serializers.BooleanField(
        default=False,
    )

    class Meta:
        """Meta definition for ItemSerializer."""

        model = Item

        fields = [
            "id",
            "point",
            "thumbnail",
            "is_gettable",
        ]

        read_only_fields = [
            "id",
            "point",
            "thumbnail",
            "is_gettable",
        ]
