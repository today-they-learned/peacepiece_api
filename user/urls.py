from django.urls import path, include

app_name = "user"

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
]
