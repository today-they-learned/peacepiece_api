from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from article.models import Article, ArticleComment
from article.serializers import ArticleCommentSerializer
from config.viewsets import BaseModelViewSet
from notification.models import Notification


class ArticleCommentViewSet(BaseModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    serializer_class = ArticleCommentSerializer
    queryset = ArticleComment.objects.all()
    ordering = ["-updated_at"]

    def perform_create(self, serializer, article_id):
        return serializer.save(writer=self.request.user, article_id=article_id)

    def perform_update(self, serializer, article_id):
        return serializer.save(writer=self.request.user, article_id=article_id)

    def create(self, request, *args, **kwargs):
        """
        댓글을 게시합니다.
        """
        article_id = kwargs["article_id"]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, article_id)
        headers = self.get_success_headers(serializer.data)
        article = get_object_or_404(Article, id=article_id)
        Notification.create_article_notification(self.request.user, article, article.writer, "challenge")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        """
        댓글의 상세 내용을 반환합니다.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        댓글 수정
        - 댓글의 게시자인 경우에만 가능합니다.
        """
        article_id = kwargs["article_id"]

        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer, article_id)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        """
        댓글을 부분적으로 수정합니다.
        - 댓글의 게시자인 경우에만 가능합니다.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        댓글을 삭제합니다.
        - 댓글의 게시자인 경우에만 가능합니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        댓글의 목록을 반환합니다.
        """
        article_id = kwargs["article_id"]

        queryset = self.get_queryset().filter(article_id=article_id)

        page = self.paginate_queryset(self.filter_queryset(queryset))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
