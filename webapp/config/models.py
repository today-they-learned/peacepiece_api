from django.db import models


class ModelManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = ModelManager()

    created_at = models.DateTimeField(
        verbose_name="추가된 일시",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="수정된 일시",
        auto_now=True,
    )
