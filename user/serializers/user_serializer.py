from django.contrib.auth import get_user_model
from rest_framework import serializers

from config.serializers import BaseModelSerializer
from item.serializers.item_serializer import ItemSerializer

User = get_user_model()


class UserSerializer(BaseModelSerializer):
    avatar = serializers.ImageField(
        use_url=True,
    )

    items = ItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "avatar",
            "items",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
        ]
