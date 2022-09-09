from rest_framework.generics import ListAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer


class WeeklyListAPIView(ListAPIView):
    queryset = Challenge.objects.weekly()
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    pagination_class = None
