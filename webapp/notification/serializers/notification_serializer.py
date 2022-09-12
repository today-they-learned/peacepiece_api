from article.serializers import ArticleAbstractSerializer
from challenge.serializers import CategorySerializer, ChallengeAbstractSerializer
from notification.models import Notification
from rest_framework import serializers
from user.serializers import UserAbstractSerializer


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer definition for Notification Model."""

    contributor = UserAbstractSerializer(read_only=True)
    article = ArticleAbstractSerializer(read_only=True)
    challenge = ChallengeAbstractSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        """Meta definition for NotificationSerializer."""

        model = Notification

        fields = [
            "id",
            "contributor",
            "article",
            "challenge",
            "category",
            "is_viewed",
            "notice_category",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "contributor",
            "article",
            "is_viewed",
            "notice_category",
            "created_at",
            "updated_at",
        ]
