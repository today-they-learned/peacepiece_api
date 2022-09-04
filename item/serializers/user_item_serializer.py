from config.serializers import BaseModelSerializer
from item.models import UserItem
from item.serializers import ItemSerializer
from user.serializers import UserSerializer


class UserItemSerializer(BaseModelSerializer):
    """Serializer definition for UserItem Model."""

    item = ItemSerializer(
        read_only=True,
    )

    user = UserSerializer(
        read_only=True,
    )

    class Meta:
        """Meta definition for UserItemSerializer."""

        model = UserItem

        fields = [
            "id",
            "user",
            "item",
            "count",
        ]

        read_only_fields = [
            "id",
            "user",
            "item",
            "count",
        ]
