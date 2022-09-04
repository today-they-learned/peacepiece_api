# Generated by Django 4.0.6 on 2022-09-04 07:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("item", "0004_alter_item_category_alter_item_name_alter_item_point_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useritem",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_items",
                to="item.item",
            ),
        ),
        migrations.AlterField(
            model_name="useritem",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_items",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
