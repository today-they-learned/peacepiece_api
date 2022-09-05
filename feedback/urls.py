from django.urls import include, path
from rest_framework.routers import DefaultRouter

from feedback.views import FeedbackViewSet

app_name = "feedback"

feedback = FeedbackViewSet.as_view(
    {
        "delete": "destroy",
        "post": "create",
    }
)


urlpatterns = [
    path("<emoji>/", feedback),
]
