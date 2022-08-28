from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
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
