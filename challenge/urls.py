from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import (
    CategoryListAPIView,
    ChallengeSuggestionFeedbackAPIView,
    ChallengeSuggestionViewSet,
    ChallengeViewSet,
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
        "categories/",
        CategoryListAPIView.as_view(),
        name="ChallengeCatgegories",
    ),
]

urlpatterns += router.urls
