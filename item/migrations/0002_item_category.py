# Generated by Django 4.0.6 on 2022-09-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("map", "map"), ("animal", "animal"), ("item", "item")], default="map", max_length=30
            ),
        ),
    ]
