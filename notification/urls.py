from django.urls import path

from notification.views import NotificationChangeAPIView, NotificationViewSet

app_name = "notification"

notification = NotificationViewSet.as_view(
    {
        "get": "get",
        "post": "post",
    }
)

urlpatterns = [path("", notification), path("<int:notification_id>/", NotificationChangeAPIView.as_view())]
