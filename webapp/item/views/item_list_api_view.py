from item.models import Item
from item.serializers import ItemListSerializer
from item.services import BuyableItemCheckService
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ItemListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemListSerializer
    queryset = Item.objects.all()

    @property
    def current_user(self):
        return self.request.user

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        buyable_item_check_results = BuyableItemCheckService(self.request).list()

        return {
            "request": self.request,
            "format": self.format_kwarg,
            "view": self,
            "buyable_item_check_results": buyable_item_check_results,
        }

    # 사용자의 조건에 맞는 아이템들만 보여주기
    def get(self, request, *args, **kwargs):
        # 사용자가 갖고 있는 아이템들

        queryset = self.get_queryset().select_related("thumbnail")
        serializer = self.get_serializer(queryset, many=True, context=self.get_serializer_context())

        return Response(serializer.data, status=status.HTTP_200_OK)
