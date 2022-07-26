from config.serializers import BaseModelSerializer
from item.models import ItemCondition
from rest_framework import serializers

from .item_condition_abstract_serializer import ItemConditionAbstractSerializer
from .item_serializer import ItemSerializer


class ItemConditionSerializer(BaseModelSerializer):
    """Serializer definition for ItemCondition Model."""

    item = ItemSerializer(
        read_only=True,
    )

    pre_item_condition = ItemConditionAbstractSerializer(
        read_only=True,
    )

    class Meta:
        """Meta definition for ItemConditionSerializer."""

        model = ItemCondition

        fields = [
            "id",
            "item",
            "max_count",
            "priority",
            "pre_item_condition",
        ]

        read_only_fields = [
            "id",
            "item",
            "max_count",
            "priority",
            "pre_item_condition",
        ]
