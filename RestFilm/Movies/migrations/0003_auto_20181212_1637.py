# Generated by Django 2.1.4 on 2018-12-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_remove_comment_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(upload_to='film_images'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='film',
            name='trailer_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='news_images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
