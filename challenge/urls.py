from django.urls import path
from challenge.views import (
    ChallengeRetrieveAPIView,
)

app_name = "challenge"

urlpatterns = [
    # path('/search',ChallengeRetrieveAPIView.as_view()),
]
