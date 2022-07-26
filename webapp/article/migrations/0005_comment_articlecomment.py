# Generated by Django 4.0.6 on 2022-08-29 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0004_alter_article_writer_alter_challengearticle_article_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="추가된 일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정된 일시")),
                ("content", models.TextField(blank=True, max_length=300, null=True, verbose_name="내용")),
                (
                    "writer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
                "db_table": "comments",
            },
        ),
        migrations.CreateModel(
            name="ArticleComment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="추가된 일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정된 일시")),
                (
                    "article",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="article_comments",
                        to="article.article",
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="article_comments",
                        to="article.comment",
                    ),
                ),
            ],
            options={
                "verbose_name": "ArticleComment",
                "verbose_name_plural": "ArticleComments",
                "db_table": "article_comments",
            },
        ),
    ]
