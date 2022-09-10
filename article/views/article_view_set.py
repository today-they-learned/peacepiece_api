from django.db import transaction
from django.db.models import Case, When
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from article.models import Article
from article.permissions import IsArticleEditableOrDestroyable
from article.serializers import ArticleListSerializer, ArticleSerializer, ArticleUpdateSerializer
from config.viewsets import BaseModelViewSet
from feedback.models import ArticleFeedback, ArticleUserFeedback
from point.models import Point


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
            "article_comments",
            "challenge__categories",
            "challenge__thumbnail",
            "challenge__images",
        )
    )
    search_fields = ["content"]
    filterset_fields = ["content", "writer", "challenge"]
    ordering_fields = []
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "retrieve":
            return ArticleSerializer
        if self.action == "update" or self.action == "partial_update":
            return ArticleUpdateSerializer

        return ArticleListSerializer

    def get_user_feedbacks(self):
        if self.is_anonymous_user:
            return []
        article = self.get_object()
        # ArticleUserFeedback.objects.filter(article=article, user=self.current_user).values_list('feedback', flat=True)
        return []

    def get_user_feedbacks_by_article_id(self):
        if self.is_anonymous_user:
            return {}
        return {}

    def get_feedbacks(self):
        if self.is_anonymous_user:
            return []
        return []

    def get_feedbacks_by_article_id(self):
        if self.is_anonymous_user:
            return {}
        return {}

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = {"request": self.request, "format": self.format_kwarg, "view": self}

        if self.action == "list" or self.action == "create":
            context["feedbacks_by_article_id"] = self.get_feedbacks_by_article_id()
            context["user_feedbacks_by_article_id"] = self.get_user_feedbacks_by_article_id()
        else:
            context["feedbacks"] = self.get_feedbacks()
            context["user_feedbacks"] = self.get_user_feedbacks()

        return context

    @transaction.atomic
    def perform_create(self, serializer):
        article = serializer.save(writer=self.request.user)

        if article.challenge is not None:

            challenge = article.challenge

            point = Point(
                user=self.current_user,
                challenge=challenge,
                article=article,
                point_category="prove_challenge",
                amount=challenge.point,
            )
            point.save()

            self.current_user.point += challenge.point
            self.current_user.save()

        return article

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
