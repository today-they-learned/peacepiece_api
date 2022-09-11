from config.views import BaseAPIView
from django.contrib.auth import get_user_model
from django.db.models import F, Sum
from django.shortcuts import get_object_or_404
from item.models import Item
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class UserItemStatusAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(User, pk=user_id)
        ret = dict([[c[0], 0] for c in Item.CATEGORY_CHOICES])

        item_statuses = (
            user.user_items.select_related("item")
            .values("item__category", "count")
            .annotate(total_count=Sum("count"), category=F("item__category"))
            .values("category", "total_count")
        )

        for item_status in item_statuses:
            ret[item_status["category"]] = item_status["total_count"]

        return Response(ret, status=status.HTTP_200_OK)
