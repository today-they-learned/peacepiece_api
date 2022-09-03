from rest_framework import serializers

from item.models import ItemCondition

from .item_serializer import ItemSerializer


class ItemConditionAbstractSerializer(serializers.ModelSerializer):
    """Serializer definition for ItemCondition Model."""

    item = ItemSerializer(
        read_only=True,
    )

    class Meta:
        """Meta definition for ItemConditionAbstractSerializer."""

        model = ItemCondition

        fields = [
            "id",
            "item",
            "max_count",
        ]

        read_only_fields = [
            "id",
            "item",
            "max_count",
        ]
