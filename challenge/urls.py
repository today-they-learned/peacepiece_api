from rest_framework.routers import DefaultRouter

from challenge.views import ChallengeSuggestionFeedbackView, ChallengeSuggestionViewSet, ChallengeViewSet

app_name = "challenge"

router = DefaultRouter()
router.register("suggestions/feedbacks", ChallengeSuggestionFeedbackView, basename="ChallengeSuggestionFeedback")
router.register("suggestions", ChallengeSuggestionViewSet, basename="ChallengeSuggestion")
router.register("", ChallengeViewSet, basename="Challenge")

urlpatterns = []

urlpatterns += router.urls
