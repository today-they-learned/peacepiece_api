from item.models import Item
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


class ItemBuyAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()

    def create(self, request, item_id, item_cnt, *args, **kwargs):
        """
        Args:
            item_id (int): 구매하고자 하는 아이템의 아이디
            item_cnt (int): 구매하고자 하는 아이템의 개수
        """

        # 포인트 차감

        return super().create(request, *args, **kwargs)
