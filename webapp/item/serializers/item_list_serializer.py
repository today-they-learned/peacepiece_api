from config.serializers import BaseModelSerializer
from file_manager.serializers import ImageSerializer
from item.models import Item
from rest_framework import serializers


class ItemListSerializer(BaseModelSerializer):
    """Serializer definition for Item Model."""

    thumbnail = ImageSerializer(read_only=True)
    buyable_context = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for ItemSerializer."""

        model = Item

        fields = [
            "id",
            "name",
            "category",
            "point",
            "thumbnail",
            "buyable_context",
        ]

        read_only_fields = [
            "id",
            "name",
            "category",
            "point",
            "thumbnail",
            "buyable_context",
        ]

    def get_buyable_context(self, obj):
        buyable_item_check_results: dict = self.context.get("buyable_item_check_results")
        return buyable_item_check_results.get(obj.id)
