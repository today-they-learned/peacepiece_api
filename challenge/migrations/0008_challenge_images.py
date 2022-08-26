# Generated by Django 4.0.6 on 2022-08-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_manager", "0002_challengeimage"),
        ("challenge", "0007_alter_challengecategory_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="images",
            field=models.ManyToManyField(
                related_name="challenges", through="file_manager.ChallengeImage", to="file_manager.image"
            ),
        ),
    ]
