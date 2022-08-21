# Generated by Django 4.0.6 on 2022-08-21 08:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0004_merge_0002_challengesuggestion_0003_challengereminder"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="추가된 일시",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
        ),
        migrations.AddField(
            model_name="challenge",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="추가된 일시",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challenge",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
        ),
        migrations.AddField(
            model_name="challengecategory",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="추가된 일시",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challengecategory",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
        ),
        migrations.AddField(
            model_name="challengereminder",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="추가된 일시",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challengereminder",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
        ),
        migrations.AddField(
            model_name="challengesuggestion",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="추가된 일시",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challengesuggestion",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
        ),
    ]
