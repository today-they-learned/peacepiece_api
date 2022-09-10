from config.models import BaseModel
from django.db import models


class Image(BaseModel):
    class Meta:
        db_table = "images"
        verbose_name = "Image"
        verbose_name_plural = "Images"

    file = models.ImageField(upload_to="images/", blank=True, null=True)
    uploader = models.ForeignKey("user.User", related_name="uploader", on_delete=models.SET_NULL, null=True, blank=True)
