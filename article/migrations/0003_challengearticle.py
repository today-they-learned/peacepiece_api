# Generated by Django 4.0.6 on 2022-08-25 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_merge_20220823_2225'),
        ('article', '0002_article_created_at_article_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='challenge_article', to='article.article')),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='challenge_article', to='challenge.challenge')),
            ],
            options={
                'verbose_name': 'ChallengeArticle',
                'verbose_name_plural': 'ChallengeArticles',
                'db_table': 'challenge_article',
            },
        ),
    ]
