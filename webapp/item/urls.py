from django.urls import path
from item.views import BuyItemAPIView, ItemListAPIView

app_name = "item"

urlpatterns = [
    path("", ItemListAPIView.as_view()),
    path("<int:item_id>/", BuyItemAPIView.as_view()),
]
