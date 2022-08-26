from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer, ChallengeSerializer
from config.viewsets import BaseViewSet


class ChallengeViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["categories"]
    search_fields = ["title"]
    ordering_fields = ["point", "prover_cnt", "created_at", "updated_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeAbstractSerializer

        return ChallengeSerializer
