# Generated by Django 4.0.6 on 2022-09-09 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0014_alter_challenge_end_at_alter_challenge_start_at"),
        ("item", "0005_alter_useritem_item_alter_useritem_user"),
        ("article", "0012_alter_articlecomment_writer"),
        ("point", "0004_alter_point_user_alter_point_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="point",
            name="article",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="points",
                to="article.article",
            ),
        ),
        migrations.AddField(
            model_name="point",
            name="challenge",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="points",
                to="challenge.challenge",
            ),
        ),
        migrations.AddField(
            model_name="point",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="points",
                to="item.item",
            ),
        ),
        migrations.AddField(
            model_name="point",
            name="point_category",
            field=models.CharField(
                choices=[("buy_item", "아이템 구매"), ("prove_challenge", "챌린지 인증 글 작성")],
                max_length=30,
                null=True,
                verbose_name="포인트 종류",
            ),
        ),
        migrations.AlterField(
            model_name="point",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]