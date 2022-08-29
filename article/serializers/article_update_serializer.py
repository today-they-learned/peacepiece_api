from django.db import transaction
from rest_framework import serializers

from file_manager.models import ArticleImage, Image

from .article_serializer import ArticleSerializer


class ArticleUpdateSerialzier(ArticleSerializer):
    image_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Image.objects.all(),
        write_only=True,
        required=False,
    )

    def clear_existing_images(self, instance, remaing_ids):
        for article_image in instance.article_images.exclude(image_id__in=remaing_ids):
            article_image.delete()

    @transaction.atomic
    def update(self, instance, validated_data):
        remaining_images = validated_data.pop("image_ids", [])
        images = validated_data.pop("images", [])

        # NOTE: image_ids 가 validation을 거쳐 Image 객체로 나옴.
        remaining_image_ids = [*map(lambda image: image.id, remaining_images)]

        self.clear_existing_images(instance, remaining_image_ids)

        for image_file in images:
            image = Image(file=image_file["file"])
            image.save()
            ArticleImage.objects.get_or_create(article=instance, image=image)

        return super().update(instance, validated_data)

    class Meta(ArticleSerializer.Meta):
        fields = [
            "id",
            "writer",
            "content",
            "image_ids",
            "images",
            "created_at",
            "updated_at",
        ]
