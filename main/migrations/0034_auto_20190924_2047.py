# Generated by Django 2.2.3 on 2019-09-25 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20190923_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewableproduct',
            name='category',
            field=models.CharField(default='frame', max_length=100),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 24, 20, 47, 17, 583880), verbose_name='date published'),
        ),
    ]
