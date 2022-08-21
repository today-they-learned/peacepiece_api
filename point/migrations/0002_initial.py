# Generated by Django 4.1 on 2022-08-14 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("point", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="point",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="point",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
