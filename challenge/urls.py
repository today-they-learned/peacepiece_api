from django.urls import path

from .views import ChallengeRetrieveAPIView

app_name = "challenge"

urlpatterns = [
    path('',ChallengeRetrieveAPIView.as_view())
]
