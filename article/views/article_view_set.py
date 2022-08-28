from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from article.serializers import ArticleListSerializer, ArticleSerializer
from article.permissions import IsArticleEditableOrDestroyable
from article.models import Article

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleListSerializer
    permission_classes = [
        IsAuthenticated,
        IsArticleEditableOrDestroyable,
    ]
    queryset = Article.objects.all().select_related('writer')
    filterset_fields = ['content']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-updated_at']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ArticleSerializer

        return ArticleListSerializer

    def perform_create(self, serializer):
        return serializer.save(writer=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        글을 게시합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        글의 상세 내용을 반환합니다.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        글을 수정합니다.
        - 글의 게시자인 경우에만 가능합니다.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        글의 상세 내용을 반환합니다.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        글을 삭제합니다.
        - 글의 게시자인 경우에만 가능합니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        글의 목록을 반환합니다.
        """
        queryset = self.filter_queryset(self.get_queryset().filter(writer=self.request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
