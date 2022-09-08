from rest_framework.generics import ListAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer, ChallengeSerializer


class ChallengeWeeklyListAPIView(ListAPIView):
    queryset = Challenge.objects.weekly()
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeAbstractSerializer

        return ChallengeSerializer
