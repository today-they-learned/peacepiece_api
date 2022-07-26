# Generated by Django 4.0.6 on 2022-08-20 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("challenge", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChallengeSuggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, max_length=300, null=True, verbose_name="내용"),
                ),
                (
                    "feedback_cnt",
                    models.PositiveIntegerField(default=0, verbose_name="피드백 개수"),
                ),
                (
                    "challenge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="challenge_suggestion",
                        to="challenge.challenge",
                        verbose_name="챌린지",
                    ),
                ),
                (
                    "suggester",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="challenge_suggestion",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="제안자",
                    ),
                ),
            ],
            options={
                "verbose_name": "ChallengeSuggestion",
                "verbose_name_plural": "ChallengeSuggestion",
                "db_table": "challenge_suggestion",
            },
        ),
    ]
