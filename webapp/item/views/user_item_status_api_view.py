from config.views import BaseAPIView
from django.contrib.auth import get_user_model
from django.db.models import Count, F, Sum
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class UserItemStatusAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(User, pk=user_id)
        item_status = (
            user.user_items.select_related("item")
            .values("item__category", "count")
            .annotate(total_count=Sum("count"), category=F("item__category"))
            .values("category", "total_count")
        )

        return Response(item_status, status=status.HTTP_200_OK)
