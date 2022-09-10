from article.serializers import ArticleAbstractSerializer
from notification.models import Notification
from rest_framework import serializers
from user.serializers import UserAbstractSerializer


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer definition for Notification Model."""

    contributor = UserAbstractSerializer(read_only=True)
    article = ArticleAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for NotificationSerializer."""

        model = Notification

        fields = [
            "id",
            "contributor",
            "article",
            "is_viewed",
        ]

        read_only_fields = ["id", "contributor", "article", "is_viewed"]
