from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from item.models import Item, ItemCondition, UserItem
from item.serializers import BuyableItemListSerializer


class ItemAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BuyableItemListSerializer
    queryset = Item.objects.all()
    # TODO: CreateAPIView
    @property
    def current_user(self):
        return self.request.user

    def get_buyable_item_ids(self):
        user_owned_items = self.current_user.items
        buyable_item_ids = []

        item_conditions = ItemCondition.objects.all().select_related("pre_item_condition")

        for item_condition in item_conditions:
            if item_condition.is_buyable(user_owned_items):
                buyable_item_ids.append(item_condition.item_id)

        return buyable_item_ids

    # 사용자의 조건에 맞는 아이템들만 보여주기
    def get(self, request, *args, **kwargs):
        # 사용자가 갖고 있는 아이템들
        buyable_item_ids = self.get_buyable_item_ids()

        queryset = self.get_queryset().select_related("thumbnail")
        serializer = self.get_serializer(
            queryset,
            many=True,
            context={
                "buyable_item_ids": buyable_item_ids,
            },
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
