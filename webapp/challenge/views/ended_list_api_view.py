from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer
from rest_framework.generics import ListAPIView


class EndedListAPIView(ListAPIView):
    queryset = Challenge.objects.ended()
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
