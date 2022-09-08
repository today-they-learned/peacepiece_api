from rest_framework.generics import ListAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer, ChallengeSerializer


class ChallengeEndedListAPIView(ListAPIView):
    queryset = Challenge.objects.ended()
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeAbstractSerializer

        return ChallengeSerializer
