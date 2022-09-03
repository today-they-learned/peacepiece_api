# Generated by Django 4.0.6 on 2022-09-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_item_category"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="useritem",
            constraint=models.UniqueConstraint(fields=("user", "item"), name="unique_item_by_user"),
        ),
    ]
