from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer
from rest_framework.generics import ListAPIView


class DailyListAPIView(ListAPIView):
    queryset = Challenge.objects.daily()[:3]
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    pagination_class = None
