# Generated by Django 4.2.14 on 2024-07-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_articles_album_artist_articles_album_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='article',
            new_name='article_id',
        ),
    ]
