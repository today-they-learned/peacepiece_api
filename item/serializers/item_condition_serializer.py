from rest_framework import serializers

from item.serializers import ItemSerializer, ItemConditionAbstractSerializer
from item.models import ItemCondition



class ItemConditionSerializer(serializers.ModelSerializer):
    """Serializer definition for ItemCondition Model."""

    item = ItemSerializer(
        read_only = True,
    )

    pre_item_condition = ItemConditionAbstractSerializer(
        read_only = True,
    )

    class Meta:
        """Meta definition for ItemConditionSerializer."""

        model = ItemCondition

        fields = [
            "id",
            "item",
            "max_count",
            "pre_item_condition"
        ]

        read_only_fields = [
            "id",
            "item",
            "max_count",
            "pre_item_condition",
        ]
