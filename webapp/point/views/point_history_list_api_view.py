from config.views import BaseAPIView
from point.models import Point
from point.serializers.point_serializer import PointSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class PointHistoryListAPIView(ListAPIView, BaseAPIView):
    serializer_class = PointSerializer
    filterset_fields = []
    search_fields = []
    ordering_fields = []
    permission_classes = [IsAuthenticated]
    ordering = "-updated_at"

    def get_queryset(self):
        return Point.objects.filter(user=self.current_user)

    def list(self, request, *args, **kwargs):
        """
        포인트 이력 리스트 API
        : 최신순으로 반환
        """
        return super().list(self, request, args, kwargs)
