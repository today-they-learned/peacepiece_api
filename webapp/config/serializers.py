from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    @property
    def current_user(self):
        return self.context.get("request").user

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous

    @property
    def is_authenticated(self):
        return self.current_user.is_authenticated
