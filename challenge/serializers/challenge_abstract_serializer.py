from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from article.models import Article
from challenge.models import Challenge
from config.serializers import BaseModelSerializer
from file_manager.serializers import ImageSerializer

from .category_serializer import CategorySerializer


class ChallengeAbstractSerializer(BaseModelSerializer):
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

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_proved(self, challenge) -> bool:
        if self.is_anonymous_user:
            return False
        return Article.objects.filter(writer=self.current_user, challenge=challenge).exists()
