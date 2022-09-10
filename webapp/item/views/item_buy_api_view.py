from item.models import Item
from item.serializers import BuyableItemListSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ItemBuyAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = BuyableItemListSerializer
    queryset = Item.objects.all()

    def create(self, request, item_id, item_cnt, *args, **kwargs):
        """
        Args:
            item_id (int): 구매하고자 하는 아이템의 아이디
            item_cnt (int): 구매하고자 하는 아이템의 개수
        """

        # 포인트 차감

        return super().create(request, *args, **kwargs)
