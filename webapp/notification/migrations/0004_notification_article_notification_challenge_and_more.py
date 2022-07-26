# Generated by Django 4.0.6 on 2022-09-07 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0013_rename_feedback_cnt_challengesuggestion_feedback_count"),
        ("article", "0012_alter_articlecomment_writer"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notification", "0003_alter_notification_user_alter_notification_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="article",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="article.article"),
        ),
        migrations.AddField(
            model_name="notification",
            name="challenge",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="challenge.challenge"),
        ),
        migrations.AddField(
            model_name="notification",
            name="contributor",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="notice_category",
            field=models.IntegerField(
                choices=[(0, "챌린지 인증글 댓글 알림"), (1, "피스글 댓글 알림"), (2, "카테고리 챌린지 알림")], default=0, verbose_name="알림 종류"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="category",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="challenge.category"),
        ),
    ]
