from challenge.views import (
    CategoryListAPIView,
    ChallengeReminderAPIView,
    ChallengeSuggestionFeedbackAPIView,
    ChallengeSuggestionViewSet,
    ChallengeViewSet,
    DailyListAPIView,
    EndedListAPIView,
    RecommendListAPIView,
    RelatedListAPIView,
    WeeklyListAPIView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter

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
        DailyListAPIView.as_view(),
        name="ChallengeDaily",
    ),
    path(
        "recommend/",
        RecommendListAPIView.as_view(),
        name="ChallengeRecommend",
    ),
    path(
        "weekly/",
        WeeklyListAPIView.as_view(),
        name="ChallengeWeekly",
    ),
    path(
        "ended/",
        EndedListAPIView.as_view(),
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
    path(
        "<int:challenge_id>/related_challenges/",
        RelatedListAPIView.as_view(),
        name="RelatedChallenges",
    ),
]

urlpatterns += router.urls
