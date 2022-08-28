from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import ChallengeSuggestionFeedbackView, ChallengeSuggestionViewSet, ChallengeViewSet

app_name = "challenge"

router = DefaultRouter()
router.register("", ChallengeViewSet, basename="Challenge")
router.register("suggestion", ChallengeSuggestionViewSet, basename="ChallengeSuggestion")
router.register("suggestion/feedback", ChallengeSuggestionFeedbackView, basename="ChallengeSuggestionFeedback")

urlpatterns = []

urlpatterns += router.urls
