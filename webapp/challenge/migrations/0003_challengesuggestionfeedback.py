# Generated by Django 4.0.6 on 2022-08-21 07:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("challenge", "0002_challengesuggestion"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChallengeSuggestionFeedback",
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
                    "suggestion",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="challenge_suggestion_feedback",
                        to="challenge.challengesuggestion",
                        verbose_name="챌린지 제안",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="challenge_suggestion_feedback",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="피드백 유저",
                    ),
                ),
            ],
            options={
                "verbose_name": "ChallengeSuggestionFeedback",
                "verbose_name_plural": "ChallengeSuggestionFeedback",
                "db_table": "challenge_suggestion_feedback",
            },
        ),
    ]