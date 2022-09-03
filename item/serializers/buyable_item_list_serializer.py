from rest_framework import serializers
from  rest_framework.fields import empty

from file_manager.serializers import ImageSerializer
from item.models import Item


class BuyableItemListSerializer(serializers.ModelSerializer):
    """Serializer definition for Item Model."""

    thumbnail = ImageSerializer(read_only=True)

    is_buyable = serializers.SerializerMethodField()

    # def __init__(self, instance=None, data=empty, buyable_item_ids=[], **kwargs):
    #     self.buyable_item_ids = buyable_item_ids
    #     kwargs.pop('buyable_item_ids')
    #     super().__init__(instance, data, kwargs)


    class Meta:
        """Meta definition for ItemSerializer."""

        model = Item

        fields = [
           "id",
           "point",
           "thumbnail",
           "is_buyable",
        ]

        read_only_fields = [
            "id",
            "point",
            "thumbnail",
            "is_buyable",
        ]

    def get_is_buyable(self, obj):
        if obj.id in self.context.get("buyable_item_ids"):
            return True

        return False
