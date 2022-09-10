from config.serializers import BaseModelSerializer
from file_manager.models import Image
from rest_framework import serializers


class ImageSerializer(BaseModelSerializer):
    # NOTE: 필요한 경우가 있는지 확인하고 추가하기
    # uploader = UserAbstractSerializer(read_only=True)
    file = serializers.ImageField(
        required=True,
        use_url=True,
        error_messages={
            "required": "이미지를 첨부해주세요.",
            "empty": "이미지를 첨부해주세요.",
            "invalid": "이미지를 첨부해주세요.",
        },
    )

    class Meta:
        model = Image
        fields = [
            "id",
            "file",
            # 'uploader',
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
