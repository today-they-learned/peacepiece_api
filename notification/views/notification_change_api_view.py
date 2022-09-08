from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationChangeAPIView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id, *args, **kwargs):
        """
        알림 하나 읽음 처리
        """
        notification = get_object_or_404(Notification, id=notification_id)

        notification.is_viewed = True
        notification.save()

        return Response(status=status.HTTP_200_OK)
