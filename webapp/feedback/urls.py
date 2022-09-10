from django.urls import include, path
from feedback.views import FeedbackViewSet
from rest_framework.routers import DefaultRouter

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
