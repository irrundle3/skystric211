# Generated by Django 2.2.3 on 2019-09-22 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20190909_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 16, 4, 48, 611004), verbose_name='date published'),
        ),
    ]