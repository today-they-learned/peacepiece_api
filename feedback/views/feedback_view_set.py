from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from article.models import Article
from article.permissions import IsArticleEditableOrDestroyable
from config.viewsets import BaseModelViewSet, BaseViewSet
from feedback.models import ArticleFeedback, ArticleUserFeedback, Feedback
from feedback.models.article_feedback import ArticleFeedback
from feedback.serializers import FeedbackSerializer


class FeedbackViewSet(BaseViewSet):

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated, IsArticleEditableOrDestroyable]

    def create(self, request, article_id, emoji, *args, **kwargs):
        article = get_object_or_404(Article, id=article_id)

        feedback = Feedback.objects.get_or_create(emoji=emoji)[0]

        article_user_feedback, is_created = ArticleUserFeedback.objects.get_or_create(
            user=request.user, feedback=feedback, article=article
        )

        if not is_created:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ArticleFeedback.increment_feedback_count(article, feedback)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, article_id, emoji):
        article = get_object_or_404(Article, id=article_id)

        feedback = get_object_or_404(Feedback, emoji=emoji)

        article_user_feedback = get_object_or_404(
            ArticleUserFeedback,
            user=request.user,
            article=article,
            feedback=feedback,
        )
        article_user_feedback.delete()
        ArticleFeedback.decrement_feedback_count(article, feedback)

        return Response(status=status.HTTP_204_NO_CONTENT)
