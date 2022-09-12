# Generated by Django 4.0.6 on 2022-09-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_user_reminder_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="mail_notifiable",
            field=models.BooleanField(default=False, verbose_name="메일 알림 설정 여부"),
        ),
    ]
