# Generated by Django 4.0.6 on 2022-09-12 02:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("challenge", "0015_challengecategory_unique_category_by_challenge"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challengereminder",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="challenge_reminders", to="challenge.category"
            ),
        ),
        migrations.AlterField(
            model_name="challengereminder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="challenge_reminders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]