from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from challenge.models import Category
from challenge.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
    ]
    search_fields = ["title"]
    pagination_class = None
