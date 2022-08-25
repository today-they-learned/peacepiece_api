from rest_framework import mixins
from rest_framework.filters import OrderingFilter

from challenge.serializers import ChallengeSuggestionSerializer, ChallengeSuggestionUpdateSerializer
from config.viewsets import BaseModelViewSet


class ChallengeSuggestionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseModelViewSet,
):
    serializer_class = ChallengeSuggestionSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-updated_at",
    ]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "update":
            return ChallengeSuggestionUpdateSerializer
        return ChallengeSuggestionSerializer

    def perform_create(self, serializer):
        return serializer.save(suggester=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        챌린지 제안 목록 반환
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        챌린지 제안 상세 정보 반환
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        챌린지를 제안하기 위한  ChallengeSuggestion 생성
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        챌린지 제안 수정
        - 본인이 작성한 챌린지만 수정 가능
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        챌린지 제안 삭제
        - 본인이 작성한 챌린지만 삭제 가능
        """
        return super().destroy(request, *args, **kwargs)
