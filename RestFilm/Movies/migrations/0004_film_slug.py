# Generated by Django 2.1.4 on 2018-12-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_auto_20181212_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]