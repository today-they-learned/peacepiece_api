from django.urls import include, path

from .views import UserRetrieveAPIView

app_name = "user"

urlpatterns = [
    path("<int:pk>/", UserRetrieveAPIView.as_view()),
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
]
