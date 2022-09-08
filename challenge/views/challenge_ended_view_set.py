from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer, ChallengeSerializer
from config.viewsets import BaseViewSet


class ChallengeEndedViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Challenge.objects.ended()
    serializer_class = ChallengeSerializer
    filterset_fields = ["categories"]
    search_fields = ["title"]
    ordering_fields = ["point", "prover_cnt", "created_at", "updated_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeAbstractSerializer

        return ChallengeSerializer
