# Generated by Django 4.0.6 on 2022-09-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0012_alter_articlecomment_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="내용"),
        ),
    ]
