from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import ChallengeViewSet

app_name = "challenge"

router = DefaultRouter()
router.register("", ChallengeViewSet, basename="Challenge")

urlpatterns = []

urlpatterns += router.urls
