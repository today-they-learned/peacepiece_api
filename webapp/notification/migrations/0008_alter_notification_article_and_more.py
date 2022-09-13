# Generated by Django 4.0.6 on 2022-09-13 02:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0013_alter_article_content"),
        ("challenge", "0016_alter_challengereminder_category_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notification", "0007_notification_is_viewed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="article",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="article.article"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="challenge.category"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="challenge",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="challenge.challenge"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="contributor",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]