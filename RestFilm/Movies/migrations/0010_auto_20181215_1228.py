# Generated by Django 2.1.4 on 2018-12-15 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0009_auto_20181215_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='photo',
            new_name='film_photo',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='photo_en',
            new_name='film_photo_en',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='photo_uk',
            new_name='film_photo_uk',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='photo',
            new_name='news_photo',
        ),
    ]
