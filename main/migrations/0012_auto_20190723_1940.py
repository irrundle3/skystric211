# Generated by Django 2.2.3 on 2019-07-24 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190723_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 19, 40, 17, 500967), verbose_name='date published'),
        ),
    ]
