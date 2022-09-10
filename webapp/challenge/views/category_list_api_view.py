from challenge.models import Category
from challenge.serializers import CategorySerializer
from rest_framework.generics import ListAPIView


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ["title"]
    pagination_class = None
