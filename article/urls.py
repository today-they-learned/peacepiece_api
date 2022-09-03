from django.urls import path
from rest_framework.routers import DefaultRouter

from article.views import ArticleCommentViewSet, ArticleViewSet

app_name = "article"

router = DefaultRouter()
router.register("(?P<article_id>\d+)/comments", ArticleCommentViewSet, basename="ArticleComment")
router.register("(?P<article_id>\d+)/comments", ArticleCommentViewSet, basename="ArticleComment")
router.register("", ArticleViewSet, basename="Article")

urlpatterns = []

urlpatterns += router.urls
