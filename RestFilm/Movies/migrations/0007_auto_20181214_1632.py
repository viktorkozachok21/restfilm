# Generated by Django 2.1.4 on 2018-12-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0006_remove_film_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='top',
            field=models.BigIntegerField(default=1),
        ),
    ]
