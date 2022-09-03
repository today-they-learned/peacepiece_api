from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from article.models import article
from challenge.models import Challenge
from file_manager.serializers import ImageSerializer

from .category_serializer import CategorySerializer


class ChallengeAbstractSerializer(serializers.ModelSerializer):
    """AbstractSerializer definition for Challenge Model."""

    categories = CategorySerializer(
        read_only=True,
        many=True,
    )
    thumbnail = ImageSerializer(read_only=True)
    is_proved = serializers.SerializerMethodField(source="is_proved")

    class Meta:
        """Meta definition for ChallengeSerializer."""

        model = Challenge
        fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
            "thumbnail",
            "is_proved",
            "start_at",
            "end_at",
        ]
        read_only_fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
            "is_proved",
            "start_at",
            "end_at",
        ]

    @property
    def current_user(self):
        return self.context.get("request").user

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_proved(self, challenge) -> bool:
        if self.is_anonymous_user:
            return False
        return article.filter(writer=self.current_user, challenge=self).exists()
