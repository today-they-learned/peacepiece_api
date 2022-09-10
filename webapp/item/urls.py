from django.urls import path
from item.views import ItemListAPIView

app_name = "item"

urlpatterns = [
    path("", ItemListAPIView.as_view()),
]
