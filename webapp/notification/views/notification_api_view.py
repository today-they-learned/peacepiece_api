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

    def get_queryset(self):
        tab = self.request.GET.get("tab")
        notifications = Notification.objects.filter(user=self.current_user).order_by("is_viewed", "-updated_at")

        if tab:
            notifications = notifications.filter(is_viewed=False)

        return notifications

    def get(self, request, *args, **kwargs):
        """
        전체 알림을 받아옴
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        알림 전체 읽음 처리
        """
        notifications = Notification.objects.filter(user=request.user, is_viewed=False).update(is_viewed=True)

        return Response(status=status.HTTP_200_OK)
