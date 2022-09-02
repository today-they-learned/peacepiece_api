from rest_framework import serializers

from article.models import ArticleComment
from user.serializers import UserAbstractSerializer


class CommentSerializer(serializers.ModelSerializer):
    """Serializer definition for Comment Model."""

    writer = UserAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for CommentSerializer."""

        model = ArticleComment
        fields = [
            "id",
            "writer",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "content",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "content": {
                "required": True,
            }
        }
