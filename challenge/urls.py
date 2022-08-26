from django.urls import path
from rest_framework.routers import DefaultRouter

from challenge.views import ChallengeListAPIView, ChallengeRetrieveAPIView

app_name = "challenge"

urlpatterns = [
    path('', ChallengeListAPIView.as_view()),
    path('/<int:pk>', ChallengeRetrieveAPIView.as_view()),
]
