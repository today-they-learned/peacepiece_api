from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback
from challenge.serializers import ChallengeSuggestionFeedbackSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings


class ChallengeSuggestionFeedbackAPIView(GenericAPIView):
    serializer_class = ChallengeSuggestionFeedbackSerializer

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, suggestion_id, *args, **kwargs):
        """
        챌린지 제안 좋아요 API
        """
        serializer = self.get_serializer(data=request.data)
        get_object_or_404(ChallengeSuggestion, pk=suggestion_id)

        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            suggestion_id=suggestion_id,
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, suggestion_id, *args, **kwargs):
        """
        챌린지 제안 좋아요 취소 API
        """
        suggestion_feedback = get_object_or_404(
            ChallengeSuggestionFeedback,
            suggestion_id=suggestion_id,
            user=self.request.user,
        )
        suggestion_feedback.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
