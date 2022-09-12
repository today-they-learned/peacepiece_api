from django.urls import path
from point.views import PointHistoryListAPIView

app_name = "point"

urlpatterns = [
    path(
        "my/",
        PointHistoryListAPIView.as_view(),
        name="PointHistory",
    ),
]
