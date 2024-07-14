# Generated by Django 4.2.14 on 2024-07-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='album_artist',
            field=models.CharField(default='example', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='album_name',
            field=models.CharField(default='example', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]