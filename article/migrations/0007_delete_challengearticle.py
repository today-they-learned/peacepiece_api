# Generated by Django 4.0.6 on 2022-08-31 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0006_merge_0005_article_images_0005_comment_articlecomment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ChallengeArticle",
        ),
    ]