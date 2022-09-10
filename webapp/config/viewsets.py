from rest_framework.viewsets import GenericViewSet, ModelViewSet


class BaseViewSet(GenericViewSet):
    @property
    def current_user(self):
        return self.request.user

    @property
    def is_authenticated_user(self):
        return self.current_user.is_authenticated

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous


class BaseModelViewSet(ModelViewSet, BaseViewSet):
    pass
