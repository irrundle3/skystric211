# Generated by Django 2.2.3 on 2019-09-24 01:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20190922_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewableproduct',
            name='active',
        ),
        migrations.RemoveField(
            model_name='reviewableproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='reviewableproduct',
            name='product_slug',
        ),
        migrations.AddField(
            model_name='reviewableproduct',
            name='imp_id',
            field=models.IntegerField(default=100000),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 23, 18, 37, 7, 964232), verbose_name='date published'),
        ),
    ]
