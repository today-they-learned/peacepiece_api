from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import (
    CategoryListAPIView,
    ChallengeDailyViewSet,
    ChallengeEndedViewSet,
    ChallengeReminderAPIView,
    ChallengeSuggestionFeedbackAPIView,
    ChallengeSuggestionViewSet,
    ChallengeViewSet,
    ChallengeWeeklyViewSet,
)

app_name = "challenge"

router = DefaultRouter()
router.register("suggestions", ChallengeSuggestionViewSet, basename="ChallengeSuggestion")
router.register("daily", ChallengeDailyViewSet, basename="ChallengeDaily")
router.register("weekly", ChallengeWeeklyViewSet, basename="ChallengeWeekly")
router.register("ended", ChallengeEndedViewSet, basename="ChallengeEnded")
router.register("", ChallengeViewSet, basename="Challenge")

urlpatterns = [
    path(
        "suggestions/<int:suggestion_id>/feedbacks/",
        ChallengeSuggestionFeedbackAPIView.as_view(),
        name="ChallengeSuggestionFeedback",
    ),
    path(
        "reminders/",
        ChallengeReminderAPIView.as_view(),
        name="ChallengeReminders",
    ),
    path(
        "categories/",
        CategoryListAPIView.as_view(),
        name="ChallengeCatgegories",
    ),
]

urlpatterns += router.urls
