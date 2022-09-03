# Generated by Django 4.0.6 on 2022-09-03 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0011_remove_articlecomment_comment_articlecomment_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlecomment",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="article_comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
    ]
