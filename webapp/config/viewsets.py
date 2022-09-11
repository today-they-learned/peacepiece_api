from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .views import BaseAPIView


class BaseViewSet(GenericViewSet, BaseAPIView):
    pass


class BaseModelViewSet(ModelViewSet, BaseViewSet):
    pass
