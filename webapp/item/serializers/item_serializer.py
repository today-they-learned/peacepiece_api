from config.serializers import BaseModelSerializer
from file_manager.serializers import ImageSerializer
from item.models import Item
from rest_framework import serializers


class ItemSerializer(BaseModelSerializer):
    """Serializer definition for Item Model."""

    thumbnail = ImageSerializer(read_only=True)

    class Meta:
        """Meta definition for ItemSerializer."""

        model = Item

        fields = [
            "id",
            "name",
            "category",
            "point",
            "thumbnail",
        ]

        read_only_fields = [
            "id",
            "name",
            "category",
            "point",
            "thumbnail",
        ]
