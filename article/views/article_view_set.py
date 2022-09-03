from django.db.models import Case, When
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from article.models import Article
from article.permissions import IsArticleEditableOrDestroyable
from article.serializers import ArticleListSerializer, ArticleSerializer, ArticleUpdateSerializer
from config.viewsets import BaseModelViewSet


class ArticleViewSet(BaseModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsArticleEditableOrDestroyable,
    ]
    queryset = (
        Article.objects.all()
        .select_related(
            "challenge",
            "writer",
        )
        .prefetch_related(
            "images",
            "challenge__categories",
            "challenge__thumbnail",
            "challenge__images",
        )
    )
    filterset_fields = ["content", "writer", "challenge"]
    ordering_fields = []
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if self.action == "create":
            return ArticleSerializer
        if self.action == "update" or self.action == "partial_update":
            return ArticleUpdateSerializer

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
        글을 부분적으로 수정합니다.
        - 글의 게시자인 경우에만 가능합니다.
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
        queryset = self.get_queryset()

        if self.is_authenticated_user and "challenge" in request.query_params:
            self.ordering = ["-my_article", "-updated_at"]
            queryset = queryset.annotate(my_article=Case(When(writer_id=request.user.id, then=1), default=0))

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
