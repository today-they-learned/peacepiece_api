# Generated by Django 4.0.6 on 2022-09-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0015_challengecategory_unique_category_by_challenge"),
        ("user", "0005_user_point"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reminder_categories",
            field=models.ManyToManyField(
                related_name="users", through="challenge.ChallengeReminder", to="challenge.category"
            ),
        ),
    ]
