from challenge.models import Category
from challenge.serializers import CategorySerializer
from config.views import BaseAPIView
from rest_framework.generics import ListAPIView


class CategoryListAPIView(ListAPIView, BaseAPIView):
    serializer_class = CategorySerializer
    search_fields = ["title"]
    filterset_fields = []
    ordering_fields = []
    pagination_class = None
    # TODO: 유저가 리마인더를 설정한 경우 배제

    def get_queryset(self):
        queryset = Category.objects.all()
        if self.is_anonymous_user:
            return queryset

        reminder_category_ids = self.current_user.reminder_categories.values_list("id", flat=True)

        return queryset.exclude(id__in=reminder_category_ids)
