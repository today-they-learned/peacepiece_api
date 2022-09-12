from challenge.models import Challenge, ChallengeCategory
from challenge.serializers import ChallengeSerializer
from config.views import BaseAPIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class RecommendListAPIView(ListAPIView, BaseAPIView):
    serializer_class = ChallengeSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def get_reminder_category_ids_of_current_user(self):
        return [*self.current_user.challenge_reminders.values_list("category_id", flat=True)]

    def get_recommended_challenge_ids(self, category_ids):
        return [*ChallengeCategory.objects.filter(category_id__in=category_ids).values_list("challenge_id", flat=True)]

    def get_queryset(self):
        category_ids = self.get_reminder_category_ids_of_current_user()
        challenge_ids = self.get_recommended_challenge_ids(category_ids)
        return Challenge.objects.is_progressing().filter(pk__in=challenge_ids)[:2]

    def list(self, request, *args, **kwargs):
        """
        추천 챌린지 리스트 API
        : ChallengeReminder로 연결되어있는 category의 진행 중인 챌린지 최대 2개 반환
        """
        return super().list(self, request, args, kwargs)
