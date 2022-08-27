from django.urls import path
from rest_framework.routers import DefaultRouter

from article.views import ArticleViewSet

app_name = "article"

router = DefaultRouter()
router.register('', ArticleViewSet, basename='Article')

urlpatterns = []

urlpatterns += router.urls
