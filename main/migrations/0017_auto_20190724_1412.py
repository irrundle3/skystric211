# Generated by Django 2.2.3 on 2019-07-24 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190724_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewableproduct',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 14, 12, 59, 156205), verbose_name='date published'),
        ),
    ]
