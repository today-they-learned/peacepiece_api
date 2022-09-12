from article.models import Article
from challenge.models import Challenge
from drf_writable_nested.serializers import WritableNestedModelSerializer
from item.serializers import ItemSerializer
from point.models import Point
from rest_framework import serializers
from user.serializers import UserAbstractSerializer


class PointSerializer(WritableNestedModelSerializer):
    """Serializer definition for Point Model."""

    user = UserAbstractSerializer(
        read_only=True,
    )

    challenge_id = serializers.PrimaryKeyRelatedField(
        source="challenge",
        queryset=Challenge.objects.all(),
        write_only=True,
        required=False,
    )

    article_id = serializers.PrimaryKeyRelatedField(
        source="article",
        queryset=Article.objects.all(),
        write_only=True,
        required=False,
    )

    item = ItemSerializer(
        read_only=True,
    )

    class Meta:
        """Meta definition for PointSerializer."""

        model = Point

        fields = [
            "id",
            "user",
            "challenge_id",
            "article_id",
            "item",
            "category",
            "amount",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "challenge_id",
            "article_id",
            "item",
            "category",
            "amount",
            "created_at",
            "updated_at",
        ]
