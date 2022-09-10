from config.viewsets import BaseViewSet
from notification.models import Notification
from notification.serializers import NotificationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class NotificationViewSet(BaseViewSet):

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get(self, request, *args, **kwargs):
        """
        전체 알림을 받아옴
        """
        tab = request.GET.get("tab")

        notification_ids = Notification.objects.filter(user=request.user).values_list("id", flat=True)

        # 읽지 않은 알림 목록
        if tab:
            notification_ids = notification_ids.filter(is_viewed=False)

        queryset = self.get_queryset().filter(id__in=notification_ids)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        알림 전체 읽음 처리
        """

        notifications = Notification.objects.filter(user=request.user, is_viewed=False).update(is_viewed=True)

        return Response(status=status.HTTP_200_OK)
