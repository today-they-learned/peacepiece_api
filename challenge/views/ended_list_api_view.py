from rest_framework.generics import ListAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer


class EndedListAPIView(ListAPIView):
    queryset = Challenge.objects.ended()
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
