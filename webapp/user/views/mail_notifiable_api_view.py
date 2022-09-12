from config.views import BaseAPIView
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class MailNotifiableAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.current_user.mail_notifiable = True
        self.current_user.save()
        return Response(
            {"mail_notifiable": self.current_user.mail_notifiable},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request):
        self.current_user.mail_notifiable = False
        self.current_user.save()
        return Response(
            {"mail_notifiable": self.current_user.mail_notifiable},
            status=status.HTTP_204_NO_CONTENT,
        )
