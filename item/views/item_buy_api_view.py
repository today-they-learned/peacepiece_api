from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from item.serializers import UserItemSerializer, ItemSerializer, ItemConditionSerializer, BuyableItemListSerializer
from item.models import Item, UserItem, ItemCondition

class ItemBuyAPIView(ListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BuyableItemListSerializer
    queryset = Item.objects.all()

    # 현재 상태 확인해서 구매할 수 있는지 확인
    def check_status(self,item_condition, user_owned_items):
        if item_condition.item in user_owned_items:
            user_owned_item = UserItem.objects.filter(item = item_condition.item)[0]
            if user_owned_item.count < item_condition.max_count:
                return True
        else:
            return True
        return False

    # 이전 조건을 만족했는지 확인
    def check_condition(self,pre_item_condition, user_owned_items):
        if pre_item_condition.item in user_owned_items:
            user_owned_pre_item_condition = UserItem.objects.filter(item = pre_item_condition.item)[0]
            if user_owned_pre_item_condition.count >= pre_item_condition.max_count:
                return True
        return False

    # 사용자의 조건에 맞는 아이템들만 보여주기
    def get(self, request, *args, **kwargs):

        #갖고 있는 아이템 목록
        user_owned_item_ids = UserItem.objects.filter(
            user = request.user).values_list("item__id", flat=True)

        # 사용자가 갖고 있는 아이템들
        user_owned_items = Item.objects.filter(id__in=user_owned_item_ids)

        buyable_item_ids = []

        for item_condition in ItemCondition.objects.all():
            if not item_condition.pre_item_condition:
                if self.check_status(item_condition, user_owned_items):
                    buyable_item_ids.append(item_condition.item_id)

            else:
                pre_item_condition = item_condition.pre_item_condition

                if self.check_condition(pre_item_condition, user_owned_items) and self.check_status(item_condition, user_owned_items):
                    buyable_item_ids.append(item_condition.item_id)

        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset,
            many=True,
            context = {
                'buyable_item_ids':  buyable_item_ids,
            }
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
