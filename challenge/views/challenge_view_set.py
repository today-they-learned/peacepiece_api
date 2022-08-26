from rest_framework.generics import ListAPIView, RetrieveAPIView

from challenge.models import Challenge
from challenge.serializers import ChallengeListSerializer

class ChallengeListAPIView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ChallengeRetrieveAPIView(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer
