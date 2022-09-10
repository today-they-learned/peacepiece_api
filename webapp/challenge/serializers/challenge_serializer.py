from file_manager.serializers import ImageSerializer

from .challenge_abstract_serializer import ChallengeAbstractSerializer


class ChallengeSerializer(ChallengeAbstractSerializer):
    """Serializer definition for Challenge Model."""

    images = ImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta(ChallengeAbstractSerializer.Meta):
        """Meta definition for ChallengeSerializer."""

        fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
            "thumbnail",
            "images",
            "start_at",
            "end_at",
            "is_ended",
        ]
