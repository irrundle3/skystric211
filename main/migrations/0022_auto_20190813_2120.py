# Generated by Django 2.2.3 on 2019-08-14 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190724_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 21, 20, 40, 969806), verbose_name='date published'),
        ),
    ]
