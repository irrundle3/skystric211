# Generated by Django 2.2.3 on 2019-07-23 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190723_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 14, 33, 48, 72294), verbose_name='date published'),
        ),
    ]
