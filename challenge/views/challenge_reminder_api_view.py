from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from challenge.models import Category, ChallengeReminder
from challenge.serializers import ChallengeReminderSerializer


class ChallengeReminderAPIView(GenericAPIView):
    serializer_class = ChallengeReminderSerializer

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, category_id, *args, **kwargs):
        """
        챌린지 알림 설정 API
        """
        serializer = self.get_serializer(data=request.data)
        get_object_or_404(Category, pk=category_id)

        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            category_id=category_id,
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, category_id, *args, **kwargs):
        """
        챌린지 알림 설정 취소 API
        """
        challenge_reminder = get_object_or_404(
            ChallengeReminder,
            category_id=category_id,
            user=self.request.user,
        )

        challenge_reminder.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
