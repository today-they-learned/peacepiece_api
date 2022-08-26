# Generated by Django 4.0.6 on 2022-08-26 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_manager", "0002_challengeimage"),
        ("challenge", "0008_challenge_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="thumbnail",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="challenge",
                to="file_manager.image",
                verbose_name="썸네일",
            ),
        ),
    ]
