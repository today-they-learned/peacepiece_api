from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from item.serializers import UserItemSerializer, ItemSerializer, ItemConditionSerializer
from item.models import Item, UserItem, ItemCondition

class ItemBuyAPIView(ListAPIView, CreateAPIView):
    # authentication_classes = [IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    # 사용자의 조건에 맞는 아이템들만 보여주기
    def get(self, request, *args, **kwargs):
        user_item = UserItem.objects.get_or_create(user = request.user)

        print(user_item[0].item)

        # 처음으로 생성된 경우
        if user_item[0].item == None:
            # 가장 처음 아이템만
            item_ids = ItemCondition.objects.filter(
                pre_item_condition = None).values_list("item__id", flat=True)
        # 사용자의 상황에 맞는 아이템만
        # 조건 1. max_count 보다 cnt 가 적어야 / 조건 2. pre_condition 을 만족해야
        else:
            for item in user_item.item:
                print(item)
            item_ids = ItemCondition.objects.filter(
                pre_item_condition = None).values_list("item__id", flat=True)
        return None