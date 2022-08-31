from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from challenge.models import Category, ChallengeReminder
from challenge.serializers import ChallengeReminderSerializer


class ChallengeReminderAPIView(CreateAPIView, GenericAPIView):
    serializer_class = ChallengeReminderSerializer
    queryset = ChallengeReminder.objects.all()

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = ChallengeReminder.objects.filter(user=request.user)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        챌린지 알림 설정 취소 API
        """
        req_body = request.data

        challenge_reminder = get_object_or_404(
            ChallengeReminder,
            category_id=req_body["category_id"],
            user=self.request.user,
        )

        challenge_reminder.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
