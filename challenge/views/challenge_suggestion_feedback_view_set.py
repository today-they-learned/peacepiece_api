from rest_framework import mixins

from challenge.models import ChallengeSuggestionFeedback
from challenge.serializers import ChallengeSuggestionFeedbackSerializer
from config.viewsets import BaseViewSet


class ChallengeSuggestionFeedbackView(mixins.CreateModelMixin, mixins.DestroyModelMixin, BaseViewSet):
    queryset = ChallengeSuggestionFeedback.objects.all()
    serializer_class = ChallengeSuggestionFeedbackSerializer
    search_fields = ["suggestion", "user"]
    ordering_fields = ["suggestion", "user", "created_at", "updated_at"]

    def get_serializer_class(self):
        return ChallengeSuggestionFeedbackSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        챌린지 제안 feedback 생성
        - user는 하나의 challenge_suggestion에 하나의 feedback만 생성 가능
        """
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        챌린지 제안 feedback 삭제
        """
        return super().destroy(request, *args, **kwargs)
