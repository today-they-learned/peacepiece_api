from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import (
    CategoryListAPIView,
    ChallengeDailyListAPIView,
    ChallengeEndedListAPIView,
    ChallengeReminderAPIView,
    ChallengeSuggestionFeedbackAPIView,
    ChallengeSuggestionViewSet,
    ChallengeViewSet,
    ChallengeWeeklyListAPIView,
)

app_name = "challenge"

router = DefaultRouter()
router.register("suggestions", ChallengeSuggestionViewSet, basename="ChallengeSuggestion")
router.register("", ChallengeViewSet, basename="Challenge")

urlpatterns = [
    path(
        "suggestions/<int:suggestion_id>/feedbacks/",
        ChallengeSuggestionFeedbackAPIView.as_view(),
        name="ChallengeSuggestionFeedback",
    ),
    path(
        "daily/",
        ChallengeDailyListAPIView.as_view(),
        name="ChallengeDaily",
    ),
    path(
        "weekly/",
        ChallengeWeeklyListAPIView.as_view(),
        name="ChallengeWeekly",
    ),
    path(
        "ended/",
        ChallengeEndedListAPIView.as_view(),
        name="ChallengeEnded",
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
