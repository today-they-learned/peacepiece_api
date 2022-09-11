from rest_framework.views import APIView


class BaseAPIView(APIView):
    @property
    def current_user(self):
        return self.request.user

    @property
    def is_authenticated_user(self):
        return self.current_user.is_authenticated

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous
