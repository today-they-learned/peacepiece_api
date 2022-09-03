from rest_framework.generics import ListAPIView

from item.models import Item
from item.serializers import ItemSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    search_fields = ["name"]
    pagination_class = None
