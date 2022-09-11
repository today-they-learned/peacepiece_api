from config.views import BaseAPIView
from django.db import transaction
from django.shortcuts import get_object_or_404
from item.models import Item, UserItem
from item.serializers import ItemSerializer
from point.models import Point
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class BuyItemAPIView(CreateAPIView, BaseAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    @transaction.atomic
    def create(self, request, item_id, *args, **kwargs):
        """
        Args:
            item_id (int): 구매하고자 하는 아이템의 아이디
        """
        item = get_object_or_404(Item, pk=item_id)

        user_owned_items = self.current_user.user_items.all()

        # TODO: refactoring
        is_buyable = False
        for item_condition in item.conditions.all():
            is_buyable = is_buyable or item_condition.is_buyable(user_owned_items, self.current_user.point)

        if not is_buyable:
            return Response({"message": "구매할 수 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        user_item, _created = UserItem.objects.get_or_create(item=item, user=self.current_user)
        user_item.count += 1
        user_item.save()

        Point.objects.create(
            user=self.current_user,
            item=item,
            amount=-item.point,
            category="buy_item",
        )

        self.current_user.point -= item.point

        self.current_user.save()

        return Response({}, status=status.HTTP_200_OK)
