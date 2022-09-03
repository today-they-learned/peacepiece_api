from django.urls import path

from item.views import ItemListAPIView, ItemBuyAPIView

app_name = "item"

urlpatterns = [
    path('',ItemListAPIView.as_view()),
    path('buy/',ItemBuyAPIView.as_view()),
]
