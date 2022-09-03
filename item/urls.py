from django.urls import path

from item.views import ItemAPIView

app_name = "item"

urlpatterns = [
    path("", ItemAPIView.as_view()),
]
