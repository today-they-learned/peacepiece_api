from rest_framework.generics import ListAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer, ChallengeSerializer


class ChallengeDailyViewSet(ListAPIView):
    queryset = Challenge.objects.daily()[:3]
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeAbstractSerializer

        return ChallengeSerializer
