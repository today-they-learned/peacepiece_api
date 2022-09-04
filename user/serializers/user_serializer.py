from django.contrib.auth import get_user_model
from rest_framework import serializers

from config.serializers import BaseModelSerializer

User = get_user_model()


class UserSerializer(BaseModelSerializer):
    avatar = serializers.ImageField(
        use_url=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "avatar",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
        ]
