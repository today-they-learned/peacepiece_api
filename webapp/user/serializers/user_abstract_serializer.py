from config.serializers import BaseModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAbstractSerializer(BaseModelSerializer):
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
            "point",
            "mail_notifiable",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
            "avatar",
            "point",
            "mail_notifiable",
        ]
