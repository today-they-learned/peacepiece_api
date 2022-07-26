# Generated by Django 4.1 on 2022-08-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Point",
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
                ("amount", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Point",
                "verbose_name_plural": "Points",
                "db_table": "point",
            },
        ),
    ]
