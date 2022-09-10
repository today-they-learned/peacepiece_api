from enum import Enum
from itertools import groupby

from django.contrib.auth import get_user_model
from item.models import Item, ItemCondition
from item.serializers import ItemConditionSerializer

User = get_user_model()
INF = 9999999999


class UnBuyableReason(int, Enum):
    NONE = 0
    UNCOMPLETE_PRE_CONDITION = 1
    MAX_COUNT = 2
    NO_MONEY = 3
    SUCCESS = 999


class BuyableItemCheckService:
    def __init__(self, request):
        self.request = request

    def list(self):
        point = self.current_user.point
        user_items_dict = self._get_user_items_dict(self.current_user)

        items_by_id: dict = Item.objects.all().in_bulk()  # key: item.id, value: Item

        item_conditions = ItemCondition.objects.order_by("item_id").select_related(
            "pre_item_condition",
            "item__thumbnail",
            "pre_item_condition__item__thumbnail",
        )
        item_conditions = ItemConditionSerializer(item_conditions, many=True).data
        item_conditions_group_by_item_id = groupby(
            item_conditions,
            lambda item_condition: item_condition["item"]["id"],
        )

        buyable_check_results = {}

        for item_id, item_conditions_by_item_id in item_conditions_group_by_item_id:
            buyable_check_results[item_id] = {
                "buyable": False,
                "reason": UnBuyableReason.NONE,
                "lack_point": 0,
                "pre_condition": {
                    "priority": INF,
                },
            }
            item_conditions_list = [*item_conditions_by_item_id]
            for item_condition in item_conditions_list:
                pre_item_condition = item_condition.get("pre_item_condition", {})
                is_fulfill_pre_condition = self._is_fulfill_pre_condition(pre_item_condition, user_items_dict)
                is_fulfill_max_count_condition = self._is_fulfill_max_count_condition(item_condition, user_items_dict)
                is_fulfill_point, lack_point = self._is_fulfill_point(items_by_id[item_id], point)

                if is_fulfill_pre_condition:
                    if is_fulfill_max_count_condition:
                        if is_fulfill_point:
                            # 모든 조건이 충족된 경우 구매 가능하다.
                            buyable_check_results[item_id]["buyable"] = True
                            buyable_check_results[item_id]["reason"] = UnBuyableReason.SUCCESS
                            break
                        else:
                            # 사전 조건은 충족했으나, 포인트가 부족한 경우
                            if buyable_check_results[item_id]["reason"].value < UnBuyableReason.NO_MONEY.value:
                                buyable_check_results[item_id]["reason"] = UnBuyableReason.NO_MONEY
                                buyable_check_results[item_id]["lack_point"] = lack_point
                    else:
                        # 조건은 충족했으나, 이미 구매한 경우
                        if buyable_check_results[item_id]["reason"].value < UnBuyableReason.MAX_COUNT.value:
                            buyable_check_results[item_id]["reason"] = UnBuyableReason.MAX_COUNT
                else:
                    # 사전 조건을 충족하지 못한 경우
                    if buyable_check_results[item_id]["reason"].value <= UnBuyableReason.UNCOMPLETE_PRE_CONDITION.value:
                        buyable_check_results[item_id]["reason"] = UnBuyableReason.UNCOMPLETE_PRE_CONDITION
                        if pre_item_condition["priority"] < buyable_check_results[item_id]["pre_condition"]["priority"]:
                            buyable_check_results[item_id]["pre_condition"] = pre_item_condition

        return buyable_check_results

    @property
    def current_user(self):
        """현재 유저를 반환합니다."""
        return self.request.user

    def _get_user_items_dict(self, user):
        """사용자가 가지고 있는 아이템 목록을 item_id를 key로 하여 반환합니다."""
        return dict([(i["item_id"], i) for i in user.user_items.values()])

    def _is_fulfill_pre_condition(self, pre_condition: dict, user_items_dict: dict):
        """사전 조건을 성립하였는가를 반환합니다."""
        if pre_condition is None:
            # 사전 조건이 없는 경우, 충족한 것으로 간주한다.
            return True
        pre_condition_item_id = pre_condition.get("item", {}).get("id")
        pre_condition_item_count = pre_condition.get("max_count", 0)
        user_owned_item = user_items_dict.get(pre_condition_item_id)
        if user_owned_item is None:
            # 해당 아이템을 유저가 가지고 있지 않은 경우
            return False
        if user_owned_item["count"] < pre_condition_item_count:
            # 이전 조건을 충족하지 못한 경우
            return False
        return True

    def _is_fulfill_max_count_condition(self, item_condition: dict, user_items_dict: dict):
        """구매 가능 최대 개수보다 적은 상황인가를 반환합니다."""
        item_id = item_condition.get("item", {}).get("id")
        max_count = item_condition.get("max_count", 0)
        user_owned_item = user_items_dict.get(item_id)
        if user_owned_item is None:
            # 해당 아이템을 유저가 가지고 있지 않은 경우
            return True
        if user_owned_item["count"] >= max_count:
            # 이미 구매 개수가 많은 경우
            return False
        return True

    def _is_fulfill_point(self, item: Item, user_point):
        """포인트가 아이템의 가격보다 많은가를 반환합니다."""
        return item.point <= user_point, max(item.point - user_point, 0)
