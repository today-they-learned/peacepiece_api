from config.views import BaseAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserPointRetreiveAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"point": self.current_user.point},
            status=status.HTTP_200_OK,
        )
